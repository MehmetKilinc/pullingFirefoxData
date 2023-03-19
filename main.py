import os
def cerez():
	if os.path.exists("/root/.mozilla/firefox/oaiaksnt.default-esr/cookies.sqlite"):
		os.system("sqlitebrowser /root/.mozilla/firefox/oaiaksnt.default-esr/cookies.sqlite")
	else:
		print("dosya yok")
def sifre():
	if os.path.exists("/root/.mozilla/firefox/oaiaksnt.default-esr/logins.json"):
		os.system("cat /root/.mozilla/firefox/oaiaksnt.default-esr/logins.json | jq")
	else:
		print("dosya yok")
def gecmis():
	if os.path.exists("/root/.mozilla/firefox/oaiaksnt.default-esr/formhistory.sqlite"):
		os.system("sqlitebrowser /root/.mozilla/firefox/oaiaksnt.default-esr/formhistory.sqlite")
	else:
		print("dosya yok")
def indir():
	if os.path.exists("/root/.mozilla/firefox/oaiaksnt.default-esr/handlers.json"):
		os.system("cat /root/.mozilla/firefox/oaiaksnt.default-esr/handlers.json | jq")
	else:
		print("dosya yok")
def sertifika():
	if os.path.exists("/root/.mozilla/firefox/oaiaksnt.default-esr/cert9.db"):
		os.system("sqlitebrowser /root/.mozilla/firefox/oaiaksnt.default-esr/cert9.db")

def izin():
	if os.path.exists("/root/.mozilla/firefox/oaiaksnt.default-esr/permissions.sqlite"):
		os.system("sqlitebrowser /root/.mozilla/firefox/oaiaksnt.default-esr/permissions.sqlite")

def bookmark():
	if os.path.exists("/root/.mozilla/firefox/oaiaksnt.default-esr/places.sqlite"):
		os.system("sqlitebrowser /root/.mozilla/firefox/oaiaksnt.default-esr/places.sqlite")

menu =  """
		[1] çerezler
		[2] geçmiş
		[3] şifreler
		[4] indirmeler ve dosya türleri
		[5] sertifikalar
		[6] izinler
		[7] bookmarks
		[8] çıkış

	    """
while True:

	print(menu)
	secim = int(input("numara giriniz : "))
	if secim == 1:
		cerez()

	if secim == 2:
		gecmis()


	if secim == 3:
		sifre()

	if secim == 4:
		indir()

	if secim == 5:
		sertifika()

	if secim == 6:
		izin()

	if secim == 7:
		bookmark()

	if secim == 8:
		break

