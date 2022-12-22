class WAVideos:
    def __init__(self, dest_path="/storage/emulated/0/WA Status Videos"):
        self.dest_path = dest_path

    def scanFolder(self, path):
        import os
        self.path = path

        return os.listdir(self.path)

    def copyFiles(self, src_path):
        import os, shutil

        if not os.path.exists(self.dest_path):
            os.mkdir(self.dest_path)
        self.src_path = src_path

        for video in os.listdir(self.src_path):
            if video.endswith(".mp4"):
                shutil.copy(os.path.join(self.src_path, video), os.path.join(self.dest_path, video))

src_path = "/storage/emulated/0/WhatsApp/Media/.Statuses" #Temporary folder where whatsapp keeps status videos
dest_path = "/storage/emulated/0/WA Status Videos" #Folder where the videos should be saved
videos = WAVideos(dest_path)
videos.copyFiles(src_path)

