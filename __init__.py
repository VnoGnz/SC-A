# hallo bro :v

from modul import *

vnognz=[]

class gadag_user:
	def __init__(self,url,cookie):
		
		self.url=url
		self.cookies=cookie

	def followers(self,link,what=False):
		try:
			if what is True:
				link=req.get(link,cookies=self.cookies).text
			_=re.findall('" \/>\<div\ class\=\".."\>\<a\ href\=\"/(.*?)"\>\<span\>(.*?)</span\>',link)
			for __ in _:
				___=re.search("id=(\d*)" if "profile.php" in __[0] else "(.*?)\?",__[0])
				vnognz.append(___.group(1)+"(Vno Gnz)"+__[1] if ___ is not None else __[0]+"(Vno Gnz)"+__[1])
				print(f"\r * mengumpulkan {len(vnognz)} user, ctrl+c stop",end="")
			if "Lihat Selengkapnya" in link:
				self.followers(self.url+parser(link,"html.parser").find("a",string="Lihat Selengkapnya")["href"],True)
			return vnognz
		except: return vnognz
		
	def fl(self,link,what=False):
		try:
			if what is True:
				link=req.get(link,cookies=self.cookies).text
			_=re.findall('style\=\"vertical-align: middle"\>\<a\ class\=\"..\" href\=\"/(.*?)"\>(.*?)</a\>',link)
			for __ in _:
				vnognz.append(re.search("id=(\d*)" if "profile.php" in __ [0] else "(.*?)\?",__[0]).group(1)+"(Vno Gnz)"+__[1])
				print(f"\r * mengumpulkan {len(vnognz)} user, ctrl+c stop",end="")
			if "Lihat Teman Lain" in link:
				self.fl(self.url+parser(link,"html.parser").find("a",string="Lihat Teman Lain")["href"],True)
			return vnognz
		except: return vnognz
		
	def grup(self,link,why,what=False):
		try:
			if what is True:
				link=req.get(link,cookies=self.cookies).text
			_=re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',link)
			for __ in _:
				___=re.search("id=(\d*)" if "profile.php" in __[0] else "Angga Vno Ganteng:v",__[0])
				vnognz.append(___.group(1)+"(Vno Gnz)"+__[1] if ___ is not None else __[0]+"(Vno Gnz)"+__[1])
				print(f"\r * mengumpulkan {len(vnognz)} user, ctrl+c stop",end="")
			if "Lihat Selengkapnya" in link:
				self.grup(self.url+parser(link,"html.parser").find("a",string="Lihat Selengkapnya")["href"],why,True)
			else:
				self.get_post(f"{self.url}/groups/{why}")
			return vnognz
		except: return vnognz
	
	def get_post(self,link):
		try:
			link=req.get(link,cookies=self.cookies).text
			_=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',link)
			for __ in _:
				if "profile.php" in __[0]:
					___=re.search("profile.php\?id=(\d*)",__[0]).group(1)
					if ___ in vnognz:
						continue
					else:
						vnognz.append(___+"(Vno Gnz)"+__[1])
				else:
					___=re.search("(.*?)\?refid",__[0]).group(1)
					if ___ in vnognz:
						continue
					else:
						vnognz.append(___+"(Vno Gnz)"+__[1])
				print(f"\r * mengumpulkan {len(vnognz)} user, ctrl+c stop",end="")
			if "Lihat Postingan Lainnya" in link:
				self.get_post(self.url+parser(link,"html.parser").find("a",string="Lihat Postingan Lainnya")["href"])
		except: pass
			
	def cari(self,link,jumlah,what=False,why=False):
		try:
			if what is True:
				link=req.get(link,cookies=self.cookies).text
			_=re.findall('picture" \/>\<\/a\>\<\/td\>\<td\ class\=\".*?"\>\<a\ href\=\"\/(.*?)"\>\<div\ class\=\"..\"\>\<div\ class\=\"..\"\>(.*?)<\/div>',link)
			for __ in _:
				vnognz.append(re.search("id=(\d*)" if "profile.php" in __[0] else "(.*?)\?refid=",__[0]).group(1)+"(Vno Gnz)"+__[1])
				print(f"\r * mengumpulkan {len(vnognz)} user, ctrl+c stop",end="")
				if len(vnognz)==jumlah:
					why=True;break
			if why is False:
				if "Lihat Hasil Selanjutnya" in link:
					self.cari(parser(link,"html.parser").find("a",string="Lihat Hasil Selanjutnya")["href"],jumlah,True)
			return vnognz
		except: return vnognz
					
	def request(self,link,what=False):
		try:
			if what is True:
				link=req.get(link,cookies=self.cookies).text
			_=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',link)
			for __ in _:
				vnognz.append(re.search("uid=(\d*)" if "?uid" in __[0] else "\/(.*?)\?fref",__[0]).group(1)+"(Vno Gnz)"+__[1])
				print(f"\r * mengumpulkan {len(vnognz)} user, ctrl+c stop",end="")
			if "Lihat selengkapnya" in link:
				self.request(self.url+parser(link,"html.parser").find("a",string="Lihat selengkapnya")["href"],True)
			return vnognz
		except: return vnognz
	
	def like_post(self,link,jumlah,what=False,why=False):
		try:
			if what is True:
				link=req.get(link,cookies=self.cookies).text
			_=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"/(.*?)"\>(.*?)<\/a\>',link)
			for __ in _:
				vnognz.append(re.search("id=(\d*)",__[0]).group(1)+"(Vno Gnz)"+__[1] if "profile.php" in __[0] else __[0]+"(Vno Gnz)"+__[1])
				print(f"\r * mengumpulkan {len(vnognz)} user, ctrl+c stop",end="")
				if jumlah:
					if len(vnognz)==jumlah:
						why=True;break
			if why is False:
				if "Lihat Selengkapnya" in link:
					self.like_post(self.url+parser(link,"html.parser").find("a",string="Lihat Selengkapnya")["href"].replace("limit=10","limit=1500"),jumlah,True)
			return vnognz
		except: return vnognz
	
	
