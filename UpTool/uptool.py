import os
import sys

# Go dili ile yazılmış araçlar
packetsGo = {
    'subfinder': ['github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest', 'subfinder'],
    'assetfinder': ['github.com/tomnomnom/assetfinder@latest', 'assetfinder'],
    'httpx': ['github.com/projectdiscovery/httpx/cmd/httpx@latest', 'httpx'],
    'katana': ['github.com/projectdiscovery/katana/cmd/katana@latest', 'katana'],
    'gau': ['github.com/lc/gau@latest', 'gau'],
    'nuclei': ['github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest', 'nuclei'],
    'qsreplace': ['github.com/tomnomnom/qsreplace@latest', 'qsreplace'],
    'gf': ['github.com/tomnomnom/gf@latest', 'gf'],
    'anew': ['github.com/tomnomnom/anew@latest', 'anew'],
    'feroxbuster': ['github.com/epi052/feroxbuster@latest', 'feroxbuster'],
    'interactsh':['github.com/projectdiscovery/interactsh/cmd/interactsh-client@latest','interactsh'],
    'naabu': ['github.com/projectdiscovery/naabu/v2/cmd/naabu@latest', 'naabu'],
    'proxify': ['github.com/projectdiscovery/proxify/cmd/proxify@latest', 'proxify'],
    'uncover': ['github.com/projectdiscovery/uncover/cmd/uncover@latest', 'uncover'],
    'dnsx': ['github.com/projectdiscovery/dnsx/cmd/dnsx@latest', 'dnsx'],
    'cvemap': ['github.com/projectdiscovery/cvemap/cmd/cvemap@latest', 'cvemap'],
    'shuffledns': ['github.com/projectdiscovery/shuffledns/cmd/shuffledns@latest', 'shuffledns'],
    'notify': ['github.com/projectdiscovery/notify/cmd/notify@latest', 'notify']
}

# Python ile yazılmış araçlar
packetsPython = {
    'paramspider': ['https://github.com/devanshbatham/ParamSpider.git', 'ParamSpider'],
    'dirsearch': ['https://github.com/maurosoria/dirsearch.git', 'dirsearch'],
    'Corsy': ['https://github.com/s0md3v/Corsy.git', 'Corsy'],
    #'PoCors': ['https://github.com/hunthack3r/PoCors.git', 'PoCors'],
    'arjun': ['https://github.com/s0md3v/Arjun.git', 'Arjun'],
    'dalfox': ['https://github.com/hahwul/dalfox.git', 'dalfox'],
    'Gxss': ['https://github.com/KathanP19/Gxss.git', 'Gxss'],
    'sqlmap': ['https://github.com/sqlmapproject/sqlmap.git', 'sqlmap'],
    'JSScanner': ['https://github.com/0ang3el/js-scanner.git', 'JSScanner'],
    'tplmap': ['https://github.com/epinna/tplmap.git', 'tplmap'],
    'GitHound': ['https://github.com/tillson/git-hound.git', 'GitHound'],
    'Gitrob': ['https://github.com/michenriksen/gitrob.git', 'Gitrob'],
    'git-secrets': ['https://github.com/awslabs/git-secrets.git', 'git-secrets'],
    'massdns': ['https://github.com/blechschmidt/massdns.git', 'massdns'],
    'Knockpy': ['https://github.com/guelfoweb/knock.git', 'Knockpy'],
    'Sublist3r': ['https://github.com/aboul3la/Sublist3r.git', 'Sublist3r'],
    'masscan': ['https://github.com/robertdavidgraham/masscan.git', 'masscan'],
    'Sn1per': ['https://github.com/1N3/Sn1per.git', 'Sn1per'],
    'wfuzz': ['https://github.com/xmendez/wfuzz.git', 'wfuzz'],
    'patator': ['https://github.com/lanjelot/patator.git', 'patator'],
    'datasploit': ['https://github.com/DataSploit/datasploit.git', 'datasploit'],
    'hydra': ['https://github.com/vanhauser-thc/thc-hydra.git', 'hydra'],
    'changeme': ['https://github.com/ztgrace/changeme.git', 'changeme'],
    'MobSF': ['https://github.com/MobSF/Mobile-Security-Framework-MobSF.git', 'MobSF'],
    'Apktool': ['https://github.com/iBotPeaches/Apktool.git', 'Apktool'],
    'dex2jar': ['https://sourceforge.net/projects/dex2jar/', 'dex2jar'],
    'oxml_xxe': ['https://github.com/BuffaloWill/oxml_xxe.git', 'oxml_xxe'],
    'XXE Injector': ['https://github.com/enjoiz/XXEinjector.git', 'XXE Injector'],
    'JWT Toolkit': ['https://github.com/ticarpi/jwt_tool.git', 'JWT Toolkit'],
    'ssrfDetector': ['https://github.com/JacobReynolds/ssrfDetector.git', 'ssrfDetector'],
    'LFISuit': ['https://github.com/D35m0nd142/LFISuite.git', 'LFISuit'],
    'GitTools': ['https://github.com/internetwache/GitTools.git', 'GitTools'],
    'dvcs-ripper': ['https://github.com/kost/dvcs-ripper.git', 'dvcs-ripper'],
    'tko-subs': ['https://github.com/anshumanbh/tko-subs.git', 'tko-subs'],
    'HostileSubBruteforcer': ['https://github.com/nahamsec/HostileSubBruteforcer.git', 'HostileSubBruteforcer'],
    'ysoserial': ['https://github.com/frohoff/ysoserial.git', 'ysoserial'],
    'PHPGGC': ['https://github.com/ambionics/phpggc.git', 'PHPGGC'],
    'CORStest': ['https://github.com/RUB-NDS/CORStest.git', 'CORStest'],
    'retire-js': ['https://github.com/RetireJS/retire.js.git', 'retire-js'],
    'getsploit': ['https://github.com/vulnersCom/getsploit.git', 'getsploit'],
    'Findsploit': ['https://github.com/1N3/Findsploit.git', 'Findsploit'],
    'bfac': ['https://github.com/mazen160/bfac.git', 'bfac'],
    'WPScan': ['https://github.com/wpscanteam/wpscan.git', 'WPScan'],
    'CMSMap': ['https://github.com/Dionach/CMSmap.git', 'CMSMap'],
    'Amass': ['https://github.com/OWASP/Amass.git', 'Amass'],
    'spiderfoot': ['https://github.com/smicallef/spiderfoot.git', 'spiderfoot'],
    'spynner': ['https://github.com/makinacorpus/spynner.git', 'spynner'],
    'xsstrike': ['https://github.com/s0md3v/XSStrike.git', 'XSStrike'],
    'hatcloud': ['https://github.com/HatBashBR/HatCloud.git', 'hatcloud'],
    'bypass-403': ['https://github.com/iamj0ker/bypass-403.git', 'bypass-403'],
    'dotdotpwn': ['https://github.com/wireghoul/dotdotpwn.git', 'dotdotpwn'],
    'CloudPeler': ['https://github.com/pestax/cloudpeler.git', 'CloudPeler'],
    'FavFreak': ['https://github.com/devanshbatham/FavFreak.git', 'FavFreak'],
    'ghauri': ['https://github.com/r0oth3x49/ghauri.git', 'ghauri'],
    'skipfish': ['https://github.com/spinkham/skipfish.git', 'skipfish'],
    'SecretFinder': ['https://github.com/m4ll0k/SecretFinder.git', 'SecretFinder'],
    'httprobe': ['https://github.com/tomnomnom/httprobe.git', 'httprobe'],
    'openredirex': ['https://github.com/devanshbatham/OpenRedireX.git', 'openredirex'],
    'FGDSH.sh': ['https://github.com/1N3/FDGS.sh.git', 'FGDSH.sh'],
    'injectx.py': ['https://github.com/credmp/sql_injectx.git', 'injectx.py'],
    'sniper': ['https://github.com/1N3/Sn1per.git', 'Sn1per'],
    'SSrfmap.py': ['https://github.com/swisskyrepo/SSRFmap.git', 'SSrfmap.py'],
    'sqlifinder.py': ['https://github.com/patator/sqlifinder.git', 'sqlifinder.py'],
    'urldedube': ['https://github.com/s0md3v/urldedupe.git', 'urldedupe'],
    'cloudfail': ['https://github.com/m0rtem/CloudFail.git', 'cloudfail'],
    'w3af': ['https://github.com/andresriancho/w3af.git', 'w3af']
}

def installation(packetName, packetFoldername, installCode, language) -> str:
    os.chdir('/opt/')
    print(f' [UpTool] Installing {packetName}      language [{language}]')
    if language == 'python':
        os.system(f'git clone {installCode}')
        os.chdir(packetFoldername)
        os.system('pip install -r requirements.txt')
        os.system('python3 setup.py build')
        os.system('python3 setup.py install')
        os.chdir('..')
    elif language == 'go':
        os.system(f'go install -v {installCode}')
        print(f' [UpTool] {packetName} installed!')

def install_tools(tools_dict):
    for tool_name, details in tools_dict.items():
        installation(tool_name, details[1], details[0], 'python' if 'git' in details[0] else 'go')

def install_top_10():
    # İlk 10 aracı kurmak için
    top_10_tools = list(packetsPython.items())[:5] + list(packetsGo.items())[:5]
    install_tools(dict(top_10_tools))

def install_all():
    install_tools(packetsPython)
    install_tools(packetsGo)

def list_installed_tools():
    print('Installed Python tools:')
    os.system("ls /opt | grep -E 'ParamSpider|Arjun|dirsearch|Corsy|PoCors|dalfox|Gxss|JSScanner|tplmap'")
    print('\nInstalled Go tools:')
    os.system("ls ~/go/bin | grep -E 'subfinder|assetfinder|httpx|katana|nuclei|gau|qsreplace|gf|anew'")

def update_tools():
    print('Updating Python tools:')
    for tool_name, details in packetsPython.items():
        os.system(f'cd /opt/{details[1]} && git pull')
    print('\nUpdating Go tools:')
    for tool_name, details in packetsGo.items():
        os.system(f'go install -v {details[0]}')

def main():
    if len(sys.argv) < 2:
        print("Usage: uptool -t | --top, uptool -f | --full, uptool -l | --list, uptool -u | --update")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command in ['-t', '--top']:
        install_top_10()
    elif command in ['-f', '--full']:
        install_all()
    elif command in ['-l', '--list']:
        list_installed_tools()
    elif command in ['-u', '--update']:
        update_tools()
    else:
        print("Invalid command. Usage: uptool -t | --top, uptool -f | --full, uptool -l | --list, uptool -u | --update")

if __name__ == '__main__':
    main()
