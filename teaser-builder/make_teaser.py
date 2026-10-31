r"""THE GOD QUEEN - episode teaser builder.
Usage:  python make_teaser.py 1
Finds the AI clips for that episode in your Downloads folder (TGQ_Teaser_Ep01_*.mp4),
adds a title card, the episode hook, an end card with the cover, and music,
and writes claude-studio\teasers\The_God_Queen_Teaser_Ep01.mp4 (vertical 1080x1920).
Needs: Python 3, Pillow (pip install pillow), ffmpeg on PATH.
"""
import sys, os, glob, subprocess, shutil, tempfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

EPISODES = {
 "1": {
  "title": "Wedding in River Oaks, Feds at the Gate",
  "hook": "Mama Vee runs Houston from a River Oaks mansion and a can of Creole seasoning."
 },
 "2": {
  "title": "Burned Rolls-Royce and a Brother's Offer",
  "hook": "Is Boo walking into a trap?"
 },
 "3": {
  "title": "Ambush at the Pepper Stand, Gigi Is Home",
  "hook": "Boo walked into the lion's den, and Mama Vee walked into an ambush."
 },
 "4": {
  "title": "Empty Hallway: Who Guards the Queen Now?",
  "hook": "Then Gigi rolled up wearing Boo's chain."
 },
 "5": {
  "title": "War at River Oaks and a Gun in the Tank",
  "hook": "The Thibodeaux family went to the mattresses."
 },
 "6": {
  "title": "Four Shots on Bellaire, a Road to Exile",
  "hook": "Isaiah Thibodeaux will never wear a badge again."
 },
 "7": {
  "title": "Love on the Bayou While Houston Burns",
  "hook": "Isaiah found love in the bayou while Houston burned."
 },
 "8": {
  "title": "Blood at the Train Tracks, Big Dre Falls",
  "hook": "Big Dre went out the way he lived, swinging until the end."
 },
 "9": {
  "title": "Burying Big Dre, Making Peace With Royce",
  "hook": "Mama Vee buried her firstborn while the whole Fifth Ward danced him home."
 },
 "10": {
  "title": "A Bayou Wedding as Houston Plans Peace",
  "hook": "Isaiah married Josette in a little white church on the bayou and found pure happiness for one week."
 },
 "11": {
  "title": "Fire on the Bayou and the Price of a Lie",
  "hook": "Josette grabbed the keys, stuck her tongue out at Isaiah, and turned them."
 },
 "12": {
  "title": "The Summit on the Brazos and a Bad Deal",
  "hook": "One hunting lodge on the Brazos."
 },
 "13": {
  "title": "Isaiah Comes Home to Houston a New Man",
  "hook": "Isaiah came home with scars on his face and ice in his eyes."
 },
 "14": {
  "title": "One Year Later, a New King in River Oaks",
  "hook": "Isaiah has a wife, a baby boy, and forty-million-dollar deals."
 },
 "15": {
  "title": "Lake Charles Casino, a Cousin's Choice",
  "hook": "Gigi recruited an old friend behind the bar, and Rusty's phone calls led straight to Royce and Smoke Ellison."
 },
 "16": {
  "title": "Mama Vee's Warning in the Pepper Garden",
  "hook": "Mama Vee finally told the whole story."
 },
 "17": {
  "title": "The God Queen's Last Day in the Garden",
  "hook": "Mama Vee wrote four letters before dawn and danced with Cornelius to their wedding song."
 },
 "18": {
  "title": "A Queen's Funeral and the Traitor Speaks",
  "hook": "Mama Vee left four letters."
 },
 "19": {
  "title": "A Baptism While Gigi Settles Every Debt",
  "hook": "While Isaiah stood at the baptismal font renouncing Satan, every debt was paid."
 },
 "20": {
  "title": "Darnell Pays for Dre and the Door Closes",
  "hook": "Darnell confessed in church and thought he was getting a plane ticket."
 },
 "21": {
  "title": "First Communion, Bullets Through Glass",
  "hook": "Fifteen-year-old Vivian walked barefoot out of jail and sold her first bowl of gumbo for fifty cents."
 },
 "22": {
  "title": "An Old Man in San Antonio Pours Coffee",
  "hook": "Sixteen-year-old Vivian met a shy young man who bought her whole pot of gumbo just to talk to her."
 },
 "23": {
  "title": "A Senator's Bad Night and Cancún Secrets",
  "hook": "Then in Mexico, Junior got drunk and said too much."
 },
 "24": {
  "title": "Midnight in Cancún and Savannah's Secret",
  "hook": "Then he came home to Savannah in a hospital bed."
 },
 "25": {
  "title": "Savannah's Truth and Junior's Confession",
  "hook": "In the present, Savannah told Isaiah the truth, and he broke."
 },
 "26": {
  "title": "The Senate Hearing and a Brother's Visit",
  "hook": "In the present, Isaiah lied to the United States Senate so well even Savannah almost believed him."
 },
 "27": {
  "title": "René's Silence and Savannah Says Goodbye",
  "hook": "Vivian came home to New Orleans and put a stone on every lost grave in the paupers' field."
 },
 "28": {
  "title": "Lorraine Comes Home as Cornelius Fades",
  "hook": "Young Isaiah pinned his toy sheriff's badge on Mama Vee's robe, and she hired a gambler named Teddy."
 },
 "29": {
  "title": "Cornelius Keeps His Promise on the Lake",
  "hook": "Ten-year-old Isaiah cried over a redfish, and Cornelius let it go."
 },
 "30": {
  "title": "Burying the Smiling Face on Every Can",
  "hook": "Young Cornelius took Vivian's name at a backyard wedding under paper lanterns."
 },
 "31": {
  "title": "René's Last Stand at His Kitchen Door",
  "hook": "René drove fourteen-year-old Gigi to the bayou and visited every month for four years."
 },
 "32": {
  "title": "Galveston Bay and the Fifty-Two Steps",
  "hook": "Aunt Vivian took eight-year-old Junior's hand at his mother's grave."
 },
 "33": {
  "title": "Twelve Years Later, Dre's Son Comes Home",
  "hook": "Isaiah is gray, rich, and almost respectable."
 },
 "34": {
  "title": "Trumpet in the Rain, a Call at Midnight",
  "hook": "Some love can't walk through the front door."
 },
 "35": {
  "title": "Seven Empty Chairs Atop The Queen Casino",
  "hook": "Isaiah tried to buy his way out clean."
 },
 "36": {
  "title": "One Word Scratched Into the Pralines Box",
  "hook": "The sweetest smile can hide the longest grudge."
 },
 "37": {
  "title": "Isaiah's Confession in a Room of Coffins",
  "hook": "Some men carry their sins so long they forget how heavy they are."
 },
 "38": {
  "title": "Thaddeus Fontenot, Last Name on the List",
  "hook": "The truth costs something, but lies cost more."
 },
 "39": {
  "title": "A Killer From Marseille Lands in Houston",
  "hook": "Isaiah asked Dante to give up the one thing he found on his own, and it broke them both."
 },
 "40": {
  "title": "A Kiss at Josette's Grave, a Rifle Waits",
  "hook": "Forgiveness isn't saying what happened was okay."
 },
 "41": {
  "title": "Silent Night From the Rosenberg Steeple",
  "hook": "Isaiah kept a stuffed alligator in his desk for twelve years because it was the only piece of his son he had."
 },
 "42": {
  "title": "O Holy Night and a Rifle in the Steeple",
  "hook": "A trumpet fills a dark church with candlelight."
 },
 "43": {
  "title": "Christmas Midnight on the Church Steps",
  "hook": "Savannah saw the danger first, and she stepped in front of the man she loved without a second thought."
 },
 "44": {
  "title": "One Got Away, and Dante Takes the Rosary",
  "hook": "Grief changes the shape of a family."
 },
 "45": {
  "title": "The Pepper Monster Laughs One Last Time",
  "hook": "Vivian built a crown out of gumbo and grief."
 },
 "46": {
  "title": "The Fifteenth Stone and a Yellow Ribbon",
  "hook": "Dante finally sat in the chair."
 },
 "47": {
  "title": "A Fire Alarm on Chartres, Vee Is Missing",
  "hook": "Some love watches from the dark, and some love tells the truth even when it costs everything."
 },
 "48": {
  "title": "Ice Cream in a Dead Woman's Old Kitchen",
  "hook": "Celine Beaumont named her partner, then answered one knock too many."
 },
 "49": {
  "title": "The Old Legionnaire Finally Moves Again",
  "hook": "Twenty-three years ago, an old soldier sat in a parking lot and didn't move."
 },
 "50": {
  "title": "Nobody's Next, and the Sixteenth Stone",
  "hook": "Vee wears Boo's chain now, and the stones stop at sixteen."
 },
 "51": {
  "title": "Box Thirty-One and the Girl With a Chain",
  "hook": "Fifteen years later, Vee is a federal intern who wants to put criminals away."
 },
 "52": {
  "title": "Dante's Confession on a Cemetery Curb",
  "hook": "Then Dante sits on a curb, presses record on his phone, and says it all once, with no softening."
 },
 "53": {
  "title": "Lucien's Hat Band and a Plate of Tamales",
  "hook": "Aunt Gigi left Vee one last letter in a tin box, and it pointed to a gray felt hat on the porch rail."
 },
 "54": {
  "title": "The Crown Room Is Lit Again at Midnight",
  "hook": "Lorraine is alive, barely, and the tamales were poisoned."
 },
 "55": {
  "title": "The Empty Hand and the Last Pot of Gumbo",
  "hook": "Nicolás slides a pistol down the long table and dares Vee to be a Thibodeaux."
 }
}

W, H, FPS = 1080, 1920, 30
HERE = os.path.dirname(os.path.abspath(__file__))
STUDIO = os.path.dirname(HERE) if os.path.basename(HERE).lower() == 'teaser-builder' else HERE
COVER = os.path.join(STUDIO, 'characters', 'GodQueen_cover.png')
DOWNLOADS = os.path.join(os.path.expanduser('~'), 'Downloads')
GOLD, CREAM = (201, 163, 92), (240, 232, 214)

def font(bold, size):
    for p in (['C:/Windows/Fonts/georgiab.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'] if bold
              else ['C:/Windows/Fonts/georgia.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf']):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def wrap(d, text, f, maxw):
    lines, cur = [], ''
    for w in text.split():
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: lines.append(cur); cur = w
    lines.append(cur); return lines

def centered(d, y, text, f, fill, maxw=920, lh=1.3):
    for ln in wrap(d, text, f, maxw):
        d.text(((W - d.textlength(ln, font=f)) / 2, y), ln, font=f, fill=fill); y += int(f.size * lh)
    return y

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-1500:]); sys.exit('ffmpeg failed')

def still_clip(png, secs, out):
    run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', png, '-vf',
         f'format=yuv420p,loop=-1:1,trim=duration={secs},fade=t=in:st=0:d=0.5,fade=t=out:st={secs-0.5}:d=0.5',
         '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-an', out])

def main():
    if len(sys.argv) < 2: sys.exit('Usage: python make_teaser.py <episode number>')
    n = int(sys.argv[1]); ep = EPISODES[str(n)]
    clips = sorted(glob.glob(os.path.join(DOWNLOADS, f'TGQ_Teaser_Ep{n:02d}_*.mp4')))
    if not clips: sys.exit(f'No clips found: {DOWNLOADS}\\TGQ_Teaser_Ep{n:02d}_*.mp4')
    work = tempfile.mkdtemp(); parts = []

    # title card
    im = Image.new('RGB', (W, H), (0, 0, 0)); d = ImageDraw.Draw(im)
    y = centered(d, 640, 'THE GOD QUEEN', font(True, 92), GOLD)
    y = centered(d, y + 40, f'EPISODE {n}', font(True, 56), CREAM)
    y = centered(d, y + 50, ep['title'], font(False, 54), CREAM, maxw=900)
    centered(d, y + 80, ep['hook'], font(False, 40), (175, 165, 145), maxw=880)
    im.save(os.path.join(work, 'title.png')); still_clip(os.path.join(work, 'title.png'), 4.5, os.path.join(work, 'p0.mp4'))
    parts.append('p0.mp4')

    # AI clips, cropped to vertical, max 6 s each
    for i, c in enumerate(clips, 1):
        out = os.path.join(work, f'p{i}.mp4')
        run(['ffmpeg', '-y', '-loglevel', 'error', '-i', c, '-vf',
             'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,trim=0:6,setpts=PTS-STARTPTS,'
             'fade=t=in:st=0:d=0.3,format=yuv420p', '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', out])
        parts.append(f'p{i}.mp4')

    # end card
    im = Image.new('RGB', (W, H), (0, 0, 0))
    if os.path.exists(COVER):
        cv = Image.open(COVER).convert('RGB').resize((W, W))
        bg = ImageEnhance.Brightness(cv.resize((H, H)).filter(ImageFilter.GaussianBlur(40))).enhance(0.3)
        im.paste(bg, ((W - H) // 2, 0)); im.paste(cv, (0, 300))
    d = ImageDraw.Draw(im)
    centered(d, 1440, 'Every family has a queen.', font(False, 52), GOLD)
    y = centered(d, 1550, f'Listen to Episode {n}', font(True, 58), CREAM)
    centered(d, y, 'on Pocket FM', font(True, 58), CREAM)
    im.save(os.path.join(work, 'end.png')); still_clip(os.path.join(work, 'end.png'), 5, os.path.join(work, 'pe.mp4'))
    parts.append('pe.mp4')

    with open(os.path.join(work, 'list.txt'), 'w') as f:
        for p in parts: f.write(f"file '{p}'\n")
    run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', os.path.join(work, 'list.txt'), '-c', 'copy', os.path.join(work, 'joined.mp4')])
    music = ("aevalsrc='0.16*sin(2*PI*55*t)*(0.7+0.3*sin(2*PI*0.2*t))+0.1*sin(2*PI*82.4*t)"
             "+0.5*sin(2*PI*50*mod(t,1.1))*exp(-14*mod(t,1.1))':s=44100:d=120")
    outdir = os.path.join(STUDIO, 'teasers'); os.makedirs(outdir, exist_ok=True)
    final = os.path.join(outdir, f'The_God_Queen_Teaser_Ep{n:02d}.mp4')
    run(['ffmpeg', '-y', '-loglevel', 'error', '-i', os.path.join(work, 'joined.mp4'), '-f', 'lavfi', '-i', music,
         '-filter_complex', '[1:a]volume=0.6,afade=t=in:d=2[a]', '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-shortest', final])
    shutil.rmtree(work, ignore_errors=True)
    print('Done:', final)

if __name__ == '__main__':
    main()
