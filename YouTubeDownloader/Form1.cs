using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Windows.Forms;
using VideoLibrary;

namespace YouTubeDownloader
{
    public partial class Form1 : Form
    {
        List<string> links = new List<string>(); // Queue of links

        public Form1()
        { // This is with windows stuff, unnecessaru
            InitializeComponent();
        }

        // Initializes Variables, you can copy and paste this into any c# without the form load
        private void Form1_Load(object sender, EventArgs e)
        {// Finds the current directory
            DirectoryInfo d = new DirectoryInfo(AppDomain.CurrentDomain.BaseDirectory);
            FileInfo[] Files = d.GetFiles("*.tdef"); // .tdef is the format of the file, so it searches for it
            foreach (FileInfo file in Files)
            {// Makes a queue of all of the things that needs to be downloaded
                links.Add(file.Name.Substring(0, file.Name.Length - 5));
                File.Delete(file.Name); // Deletes the file so if a 2nd instance of this program is run, it doesn't download the same ones
            }
            foreach (string str in links)
            {
                downloadAndConvert(str); // Actually downloads and converts the files
            }
            Application.Exit(); // Exits the program
        }

        // Downloads and converts the link given
        private void downloadAndConvert(string vidLink)
        {
            var youTube = YouTube.Default; // Creates a youtube variable
            var video = youTube.GetVideo("https://www.youtube.com/watch?v=" + vidLink); // Gets the video using the youtube library
            string vidPath = AppDomain.CurrentDomain.BaseDirectory + video.FullName; // Creates the name for the file
            if (!File.Exists(vidPath.Substring(0, vidPath.Length - 14) + "``" + vidLink + ".wav")) // if the file isn't already downloaded
            {
                File.WriteAllBytes(vidPath, video.GetBytes()); // Creates the .mp4 file of the video
                Console.WriteLine(vidPath + " " + video.GetBytes().Length); // Debug stuff

                PathToFfmpeg = "ffmpeg.exe"; // Directs to ffmpeg
                ToWavFormat(vidPath, vidPath.Substring(0, vidPath.Length - 14) + "``" + vidLink + ".wav"); // Converts the vid to wav
                File.Delete(vidPath); // deletes the mp4 file
            }
        }
        public string PathToFfmpeg { get; set; } // variable for the ffmpeg, honestly should just be a final static ffmpeg.exe

        // Converts the mp4 to ffmpeg
        public void ToWavFormat(string pathToMp4, string pathToWav)
        { // Creates a new thread that opens the ffmpeg 
            var ffmpeg = new Process
            { // ffmpeg variables and hides the ffmpeg console so it's more user friendly to run in the background
                StartInfo = { UseShellExecute = false, CreateNoWindow = true, RedirectStandardInput = true, RedirectStandardOutput = true, WindowStyle = ProcessWindowStyle.Hidden
                , RedirectStandardError = true, FileName = PathToFfmpeg }
            };
            //ogg - @"-i ""{0}"" -vn -acodec libvorbis -f ogg -loglevel quiet -hide_banner -nostdin ""{1}""",
            var arguments =
                String.Format( // ffmpeg stuff to convert mp4 to wav, the above example is for ogg, look up how to do whatever format you want such as mp3
                    @"-i ""{0}"" -vn -acodec pcm_s16le -f wav -loglevel quiet -hide_banner -nostdin ""{1}""",
                    pathToMp4, pathToWav);

            ffmpeg.StartInfo.Arguments = arguments; // sets the arguments

            try
            {
                if (!ffmpeg.Start()) // starts the ffmpeg
                {
                    Debug.WriteLine("Error starting");
                    return;
                }
                var reader = ffmpeg.StandardError;
                string line;
                while ((line = reader.ReadLine()) != null) // if there are issues, it writes it to console to debug
                {
                    Debug.WriteLine(line);
                }
            }
            catch (Exception exception)
            {
                Debug.WriteLine(exception.ToString());
                return;
            }

            ffmpeg.Close(); // closes the ffmpeg
        }
    }
}
