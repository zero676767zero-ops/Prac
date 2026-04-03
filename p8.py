
HelloController
[HttpGet("{name}")]
public string GetHello(string name)
{
    return $"Hello {name} from .Net";
}

py file
import request, urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

name = input("Enter your name: ")
url = f"https://xxxx/Hello/{name}"

resp = requests.get(url, verify = False)

if resp.status_code == 200:
    print(resp.text)
else:
    print(f"Error : {resp.status_code}")



