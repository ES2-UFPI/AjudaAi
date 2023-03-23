using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using AjudaAiAPI.Context;

namespace AjudaAiAPI.Controllers
{
    [Route("/Demandums")]
    [ApiController]
    public class DemandumsController : ControllerBase
    {
        private readonly RailwayContext _context;

        public DemandumsController(RailwayContext context)
        {
            _context = context;
        }

        // GET: api/Demandums
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Demandum>>> GetDemanda()
        {
            return await _context.Demanda.ToListAsync();
        }

        // GET: api/Demandums/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Demandum>> GetDemandum(int id)
        {
            var demandum = await _context.Demanda.FindAsync(id);

            if (demandum == null)
            {
                return NotFound();
            }

            return demandum;
        }

        // PUT: api/Demandums/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutDemandum(int id, Demandum demandum)
        {
            if (id != demandum.CodDemanda)
            {
                return BadRequest();
            }

            _context.Entry(demandum).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!DemandumExists(id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return NoContent();
        }

        // POST: api/Demandums
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<Demandum>> PostDemandum(Demandum demandum)
        {
            _context.Demanda.Add(demandum);
            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateException)
            {
                if (DemandumExists(demandum.CodDemanda))
                {
                    return Conflict();
                }
                else
                {
                    throw;
                }
            }

            return CreatedAtAction("GetDemandum", new { id = demandum.CodDemanda }, demandum);
        }

        // DELETE: api/Demandums/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteDemandum(int id)
        {
            var demandum = await _context.Demanda.FindAsync(id);
            if (demandum == null)
            {
                return NotFound();
            }

            _context.Demanda.Remove(demandum);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        private bool DemandumExists(int id)
        {
            return _context.Demanda.Any(e => e.CodDemanda == id);
        }
    }
}
