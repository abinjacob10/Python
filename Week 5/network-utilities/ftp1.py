import ftplib

path = '/mirrors/ubuntu-cdimage/releases/22.10/release'
file1='SHA256SUMS'
ftp1=ftplib.FTP("ftp.heanet.ie")
ftp1.login()
ftp1.cwd(path)
print(ftp1.pwd())
ftp1.retrbinary("RETR SHA256SUMS", open('SHA256SUMS','wb').write)
ftp1.quit()
