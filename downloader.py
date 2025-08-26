
import re, yt_dlp

"""
This script downlloads a list of videos from Youtube.
The list contains the ids of the videos as found in the individual videos urls that comes after "https://youtu.be/"
Example: for "https://youtu.be/6AEvnLgRPNc" give "6AEvnLgRPNc".

"""


def extract_vids(file='pl.html'):
	"""
	Extracts the list of videos to download from a Yt playlist.
	In my example, pl.html is the inner html of the element 
		<ytd-playlist-panel-renderer></ytd-playlist-panel-renderer>
	as seen on the right pane on a laptop browser when watching a video from a playlist.
	"""
	print(f"\n=============== Extracting vids links ===\n")
	
	with open('pl.html', 'r', encoding='utf-8') as f:
		html = f.read()
	pattern = r'href="/watch\?v=([a-zA-Z0-9_-]{11})&amp;list='
	video_ids = re.findall(pattern, html)
	l = list(set(video_ids))
	print(f"\n=============== Extracted {len(l)} items ===\n")
	return l
	
def download_list(file):

	"""
	Download the videos in the list.
	"""
	vids = extract_vids(file)
	l = len(vids)
	i = 0
	for vid in vids :
		i += 1
		url = f"https://youtu.be/{vid}" # url = "https://youtu.be/6AEvlNgRPNc"
		print(f"\n========== {i}/{l} Getting {url} =====\n")
		ydl_opts = {'outtmpl': 'downloads/%(title)s.%(ext)s',}
		try:
			with yt_dlp.YoutubeDL(ydl_opts) as ydl:
				ydl.download([url])
		except Exception as xc:
			print(str(xc))

download_list('pl.html')



