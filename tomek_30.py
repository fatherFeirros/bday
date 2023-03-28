import sys, time, random, requests, os

class Tomasz:
    
    def __init__(self):
        
        url = "https://raw.githubusercontent.com/fatherFeirros/bday/main/tomasz.json"
        
        self.age = 30
        self.occupation = "Software Engineer"
        self.location = "Tychy"
        self.hobby = "Saxophone"
        self.has_wonderful_wife = True
        self.can_achive_anything_he_wants = True
        self.secret_message = dict(requests.get(url).json())
        
    def __enter__(self):
        
        return self
    
    def __exit__(self,exc_type, exc_value, traceback):
        
        time.sleep(5)
    
    def typing(self,m,m_s=100,t='fast'):
        for i in m:
            sys.stdout.write(chr(i) if type(i) == int else i)
            sys.stdout.flush()
            if t == 'slow':
                time.sleep(random.random() * random.uniform(1,10) / m_s)
            else:
                time.sleep(random.random() / m_s)
        print("")
                
    def progressbar(self,it, prefix="", size=60, out=sys.stdout):
    
        count = len(it)
        def show(j):
        
            x = int(size*j/count)
            print("{}[{}{}] {}/{}".format(prefix, "#"*x, "."*(size-x), j, count), 
                    end='\r', file=out, flush=True)
                    
        show(0)
        
        for i, item in enumerate(it):
        
            yield item
            show(i+1)
            
        print("\n", flush=True, file=out)
                
    def hacker_time(self,toolbar_width=61):
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        for i in range(3):
            
            self.typing(self.secret_message['words']['other'][i])
            
            for i in self.progressbar(range(100), "Progress: ", 40):
                time.sleep(0.07*random.random())
            
        print("Success!")
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    
    with Tomasz() as ma_urodziny:
        
        ma_urodziny.hacker_time()
        ma_urodziny.typing(ma_urodziny.secret_message['words']['start'],100,'slow')
        ma_urodziny.typing(ma_urodziny.secret_message['cake'],1000)
        ma_urodziny.typing(ma_urodziny.secret_message['words']['end'],100,'slow')