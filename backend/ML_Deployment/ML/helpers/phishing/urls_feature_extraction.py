from urllib.parse import urlparse
import lxml
import whois
import re
import time
from datetime import datetime
import enum

class Status(enum.Enum):
    legitimate=0
    phishing=1
    suspicious=2

class URLFeatureExtractor:

    def get_domain(self):
        try:
            self.domain_name = whois.whois(urlparse(self.url).netloc)
        except:
            self.domain_name = 'invalid'
        if self.domain_name is None:
            self.domain_name = 'invalid'

    def __init__(self,url):
        self.url = url
        self.get_domain()


    
    def havingIP(self):
        """If the domain part has IP then it is phishing otherwise legitimate"""
        match=re.search(
            '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  #IPv4
            '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)'  #IPv4 in hexadecimal
            '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}' #Ipv6
            ,self.url)    

        if match:
            return Status.phishing.value            
        else:
            return Status.legitimate.value            
    
    def long_url(self):
        
        if len(self.url) < 54:
            return Status.legitimate.value            
        elif len(self.url) >= 54 and len(self.url) <= 75:
            return Status.suspicious.value            
        else:
            return Status.phishing.value            
    
    def have_at_symbol(self):
        """This function is used to check whether the URL contains @ symbol or not"""
        if "@" in self.url:
            return Status.phishing.value            
        else:
            return Status.legitimate.value            
    
    def redirection(self):
        """If the url has symbol(//) after protocol then such URL is to be classified as phishing """
        if "//" in urlparse(self.url).path:
            return Status.phishing.value            
        else:
            return Status.legitimate.value            
        
    def prefix_suffix_separation(self):
        """If the domain has '-' symbol then it is considered as phishing site"""
        if "-" in urlparse(self.url).netloc:
            return Status.phishing.value            
        else:
            return Status.legitimate.value            
        
    def sub_domains(self):
        """If the url has more than 3 dots then it is a phishing"""
        if self.url.count(".") < 3:
            return Status.legitimate.value            
        elif self.url.count(".") == 3:
            return Status.suspicious.value            
        else:
            return Status.phishing.value            
        
    def shortening_service(self):
        """Tiny URL -> phishing otherwise legitimate"""
        match=re.search(
                    'bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                    'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                    'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                    'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                    'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                    'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                    'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|tr\.im|link\.zip\.net'
                    ,self.url)
        if match:
            return Status.phishing.value               
        else:
            return Status.legitimate.value
        
    def domain_registration_length(self):
        dns = 0
        if self.domain_name == 'invalid':
            dns=1
        else:
            domain_name = self.domain_name
        
        if dns == 1:
            return Status.phishing.value      
        else:
            expiration_date = domain_name.expiration_date
            today = time.strftime('%Y-%m-%d')
            today = datetime.strptime(today, '%Y-%m-%d')
            if expiration_date is None:
                return Status.phishing.value
            elif type(expiration_date) is list or type(today) is list :
                return Status.suspicious.value     #If it is a type of list then we can't select a single value from list. So,it is regarded as suspected website  
            else:
                creation_date = domain_name.creation_date
                expiration_date = domain_name.expiration_date
                if (isinstance(creation_date,str) or isinstance(expiration_date,str)):
                    try:
                        creation_date = datetime.strptime(creation_date,'%Y-%m-%d')
                        expiration_date = datetime.strptime(expiration_date,"%Y-%m-%d")
                    except:
                        return Status.suspicious.value
                registration_length = abs((expiration_date - today).days)
                if registration_length / 365 <= 1:
                    return Status.phishing.value 
                else:
                    return Status.legitimate.value 
            
    def age_domain(self):
        dns = 0
        if self.domain_name == 'invalid':
            dns=1
        else:
            domain_name = self.domain_name
        
        # if dns record not found
        if dns == 1:
            return Status.phishing.value
        else:
            creation_date = domain_name.creation_date
            expiration_date = domain_name.expiration_date
            if (isinstance(creation_date,str) or isinstance(expiration_date,str)):
                try:
                    creation_date = datetime.strptime(creation_date,'%Y-%m-%d')
                    expiration_date = datetime.strptime(expiration_date,"%Y-%m-%d")
                except:
                    return Status.suspicious.value
            # creation or expiration date does not exist
            if ((creation_date is None) or (expiration_date is None)):
                return Status.phishing.value
            # many expiration dates or creation dates
            elif ((type(expiration_date) is list) or (type(creation_date) is list)):
                return Status.suspicious.value
            else:
                ageofdomain = abs((expiration_date - creation_date).days)
                # less than 6 months
                if ((ageofdomain/30) < 6):
                    return Status.phishing.value
                else:
                    return Status.legitimate.value
     
    
    def dns_record(self):
        dns = 0
        if self.domain_name == 'invalid':
            dns=1
        else:
            domain_name = self.domain_name
        
        # if dns record not found
        if dns == 1:
            return Status.phishing.value
        else:
            return Status.legitimate.value
        
    def https_token(self):
        match=re.search('https://|http://',self.url)
        try:
            if match.start(0) is not None and match.start(0)==0:
                url=url[match.end(0):]
                match=re.search('http|https',self.url)
                if match:
                    return Status.phishing.value
                else:
                    return Status.legitimate.value
        except:
            return Status.phishing.value