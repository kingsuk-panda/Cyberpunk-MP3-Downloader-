import os
import sys
import time
import subprocess
from rich.console import Console
from rich.progress import Progress, BarColumn, TimeRemainingColumn, TransferSpeedColumn
console = Console()
output_folder = os.path.expanduser("~/Desktop/Gen/Music/")
def download_audio(url):
    os.makedirs(output_folder, exist_ok=True)
    console.print("\n💽 [bold pink]Starting Download...[/] 🚀\n")
    command = f'yt-dlp -x --audio-format mp3 -o "{output_folder}/%(playlist_title)s/%(title)s.%(ext)s" "{url}"' 
    with Progress(
        "[bold white]{task.percentage:>3.0f}%[/] ",
        BarColumn(bar_width=None, complete_style="bold magenta", style="gray35"),
        TransferSpeedColumn(),
        TimeRemainingColumn(),
    ) as progress:
        task = progress.add_task("Downloading...", total=100)
        for _ in range(100):
            progress.update(task, advance=1)
            time.sleep(0.05)
    subprocess.run(command, shell=True)
    console.print("\n💾 [bold pink]Download complete![/] ✅ Files saved to:", output_folder)
def main():
    global output_folder
    console.print("\n🌸 [bold pink]Welcome to[/] [bold white]Cyberpunk MP3 Downloader[/] 🌸\n")
    while True:
        console.print("\n💖 [bold pink]1. Download Video as MP3[/]")
        console.print("🎵 [bold pink]2. Download Playlist as MP3[/]")
        console.print("📂 [bold pink]3. Change Download Folder[/]")
        console.print("❌ [bold white]4. Exit[/]")
        choice = console.input("\n💾 [bold white]Enter your choice: [/]").strip()
        if choice == "1" or choice == "2":
            url = console.input("\n🔗 [bold pink]Enter YouTube Video/Playlist URL: [/]").strip()
            download_audio(url)
        elif choice == "3":
            output_folder = os.path.expanduser(console.input("\n📁 [bold pink]Enter new download folder path: [/]").strip())
            console.print(f"\n📂 [bold white]New download folder set to:[/] {output_folder}")
        elif choice == "4":
            console.print("\n🛸 [bold pink]Exiting... Stay Groovy! 🎧[/] 🛸")
            sys.exit()
        else:
            console.print("\n❌ [bold pink]Invalid choice. Try again.[/]")
if __name__ == "__main__":
    main()
