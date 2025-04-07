# 🎵 Cyberpunk MP3 Downloader

Cyberpunk MP3 Downloader is a sleek, console-based YouTube video and playlist downloader that extracts audio and saves it as MP3 files. With a cyberpunk-inspired UI powered by `rich`, this tool ensures a smooth and aesthetic experience.

---

## Features
- Download **YouTube videos** as MP3
- Download **entire playlists** as MP3
- Set a **custom download folder**
- Fancy **progress bar and UI** using `rich`
- Organizes downloaded files into folders

---

## Requirements

### 1. **Install Python 3**
Ensure you have Python installed:
```bash
python --version
```
If not installed, download it from [python.org](https://www.python.org/downloads/).

### 2. **Install Required Packages**
Run the following command to install dependencies:
```bash
pip install yt-dlp rich
```

### 3. **Install FFmpeg** *(Required for Audio Extraction)*
- **Linux (Debian/Ubuntu):**  
  ```bash
  sudo apt install ffmpeg
  ```
- **Linux (Arch-based):**  
  ```bash
  sudo pacman -S ffmpeg
  ```
- **Windows (Chocolatey):**  
  ```powershell
  choco install ffmpeg
  ```
- **Mac (Homebrew):**  
  ```bash
  brew install ffmpeg
  ```

---

## Usage

### **1. Run the Script**
Navigate to the script’s folder and run:
```bash
python cyberpunk_mp3_downloader.py
```
> If using Windows, replace `python` with `python3` if needed.

### **2. Main Menu Options**
```
🌸 Welcome to Cyberpunk MP3 Downloader 🌸  

💖 1. Download Video as MP3  
🎵 2. Download Playlist as MP3  
📂 3. Change Download Folder  
❌ 4. Exit  

💾 Enter your choice:  
```

#### **Option 1 - Download a Single Video as MP3**
- Select **1**, then enter the YouTube video URL.
- The program will process and download the MP3 file.

#### **Option 2 - Download a Playlist as MP3**
- Select **2**, then enter the playlist URL.
- All videos in the playlist will be downloaded as MP3 files.

#### **Option 3 - Change Download Folder**
- Select **3** to change the folder where MP3 files are saved.
- Enter a new folder path (e.g., `~/Music/` on Linux/macOS or `C:\Users\YourName\Music\` on Windows).

#### **Option 4 - Exit the Program**
- Select **4** to quit the downloader.

---

## Where Are the Files Saved?
By default, MP3 files are saved in:
📂 **Linux/macOS** → `~/Desktop/Gen/Music/`  
📂 **Windows** → `C:\Users\YourName\Desktop\Gen\Music\`  

If downloading a **playlist**, the files will be organized in a subfolder named after the playlist.

---

## Troubleshooting

### **1. Command Not Found Errors**
- If `yt-dlp` is not found, install it:
  ```bash
  pip install yt-dlp
  ```
- If `ffmpeg` is missing, install it (see above for OS-specific commands).

### **2. Download Fails or No Audio Output**
- Ensure `ffmpeg` is installed and correctly configured.
- Use the latest version of `yt-dlp` by updating it:
  ```bash
  pip install --upgrade yt-dlp
  ```

### **3. Permission Denied Errors**
- Run the script with administrator privileges:
  - **Windows**: Right-click → **Run as Administrator**
  - **Linux/macOS**: Run with `sudo`:
    ```bash
    sudo python cyberpunk_mp3_downloader.py
    ```

---

## Final Notes
💖 Enjoy high-quality MP3 downloads with ease! If you run into issues, check the dependencies and ensure your URLs are correct. 🎧  

🛸 **Exiting... Stay Groovy!** 🛸  

