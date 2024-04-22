# mailrecon
Automate bash script consisting tools for guessing or collecting email addresses given the company mail domain. It resulting in multiple email format. Email generated validity not checked. Tools required to run the script (add tools required on PATH) are listed below:
- https://github.com/m8sec/CrossLinked
- https://github.com/Josue87/EmailFinder
- https://github.com/maldevel/EmailHarvester
- python3
- add intelx apikey on intelxEmail.py

## Usage
```bash
./mailrecon.sh  corpomaildomain.txt /output/folder/
```

## OPSEC best practice
First step to guess corpo email is obtaining its mail format. It can be firstname.lastname@corpo.com, or initialfirstname.lastname@corpo.com, etc. The script generate only common mail format that possibly not applicable to your corpo target. Recon for target mail format is needed and can be achive using google dorking

```
google dorking : [corpomaildomain] mail format rocketreach
```

alternatively, email-format.com also capable to do so 
```
https://www.email-format.com/d/[corpomaildomain]/
```
