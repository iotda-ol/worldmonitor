THE GOD QUEEN — CLAUDE STUDIO
Put this folder at: C:\Users\maxpc\Projects\pocket-fm-projects\the-god-queen\claude-studio

WHAT'S INSIDE
episodes\           All 55 episodes (title, story, listener message), Episode 52 is the rewritten version that passes review.
trailer\            The_God_Queen_Trailer_Vertical.mp4 (47-second teaser made from the cover)
                    The_God_Queen_Video_Production_Kit.txt (character sheets, Episode 1 shot list, prompts)
characters\         The cover and the vertical character crops used to make the AI clips
                    (Mama Vee, Big Dre, Lorraine, Isaiah, Cornelius, Gigi)
                    GodQueen_Family_Closeups_Sheet.jpg  (labeled sheet of all six)
characters\closeups\ Square 1024x1024 face close-ups of all six family members
The_God_Queen_Show_Bible.md   Series rules, season arcs, episode guide, characters,
                    continuity bible, writing / version / video workflows, change log
teaser-builder\     One-click builder for the AI video teaser

HOW TO BUILD THE AI TEASER (one double-click)
1. Make sure these AI clips are in your Downloads folder (Claude downloaded them there from Vidu, PixVerse and Hailuo):
     GodQueen_clip1_MamaVee.mp4
     GodQueen_clip2_BigDre.mp4
     GodQueen_clip3_Hailuo_1.mp4
     GodQueen_clip3_Hailuo_2.mp4
     GodQueen_clip5_Cornelius.mp4   (optional, still generating on Hailuo)
2. Double-click teaser-builder\BUILD_TEASER.bat
   - If ffmpeg isn't installed, it installs it with winget the first time. Then double-click it again.
3. It writes The_God_Queen_AI_Teaser.mp4 in this folder and opens it.

Order of the teaser: Houston intro card, Mama Vee, Big Dre, Lorraine, Isaiah, Cornelius,
the "Save me a plate, Mama" text message, then the cover end card. Vertical 1080x1920, about 35 seconds, with music.

IF LORRAINE AND ISAIAH ARE SWAPPED
Hailuo saved both clips with similar names. If the bride shows up with Isaiah's caption,
open teaser-builder\clips\, swap the names 3_Lorraine.mp4 and 4_Isaiah.mp4, delete the work\ folder, and run BUILD_TEASER.bat again.

WHERE THE CLIPS CAME FROM (all free credits)
Mama Vee  — Vidu Q4 (free 1080p trial)
Big Dre   — PixVerse V6
Lorraine, Isaiah, Cornelius — Hailuo MiniMax H3

DAILY EPISODE TEASERS (one per episode, free)
Every day Claude makes 2 to 4 short AI clips for the next episode with your cover faces,
on free credits, and saves them to Downloads as TGQ_Teaser_Ep01_1.mp4, TGQ_Teaser_Ep01_2.mp4 ...
1. Double-click teaser-builder\BUILD_EPISODE_TEASER.bat
2. Type the episode number and press Enter.
3. It writes teasers\The_God_Queen_Teaser_Ep01.mp4: episode title card with the hook,
   the AI clips, then the cover end card "Listen to Episode 1 on Pocket FM", with music.
   About 25 to 35 seconds, vertical 1080x1920, ready for TikTok, Reels and Shorts.
