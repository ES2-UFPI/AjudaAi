using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using MySql.Data.MySqlClient;
using System.Security.Cryptography.X509Certificates;

namespace AjudaAiAPI.Controllers
{
    [Route("/")]
    [ApiController]
    public class ConnectionController : ControllerBase
    {       
        private readonly IConfiguration _configuration;
        
        public ConnectionController(IConfiguration configuration) { _configuration = configuration; }
        [HttpGet]
        public ActionResult<object> TestarConexao()
        {
            string status = "nothing happened";
            try
            {

                var connectionStr = _configuration["ConnectionStrings:Railway"];
                MySqlConnection connection = new MySqlConnection();
                connection.ConnectionString = connectionStr;
                connection.Open();
                status = "connected";
            }
            catch (MySqlException ex)
            {
                status = ex.Message;
                Console.WriteLine(ex.Message);
                throw;
            }

            return status;

        }
    }
}
