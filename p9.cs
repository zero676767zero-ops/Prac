using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Http;

namespace ConsoleApp2
{
    class Program
    {
        static async Task Main()
        {
            try
            {
                var client = new HttpClient();
                var response = await client.GetAsync("http://127.0.0.1:8000/hello?name=Addsksi");
                Console.WriteLine("Status: " + response.StatusCode);

                var content = await response.Content.ReadAsStringAsync();

                Console.WriteLine("Response from Python API:");
                Console.WriteLine(content);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
            Console.ReadLine();
        }
    }
}


from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello(name : str = "World"):
    return {"message" : f"Hello {name} from python"}
