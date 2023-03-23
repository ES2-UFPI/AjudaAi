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
    [Route("api/[controller]")]
    [ApiController]
    public class DemandasController : ControllerBase
    {
        private readonly RailwayContext _context;

        public DemandasController(RailwayContext context)
        {
            _context = context;
        }

        // GET: api/Demandas
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Demandum>>> GetDemanda()
        {
          if (_context.Demanda == null)
          {
              return NotFound();
          }
            return await _context.Demanda.ToListAsync();
        }

        // GET: api/Demandas/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Demandum>> GetDemandum(int id)
        {
          if (_context.Demanda == null)
          {
              return NotFound();
          }
            var demandum = await _context.Demanda.FindAsync(id);

            if (demandum == null)
            {
                return NotFound();
            }

            return demandum;
        }

        // PUT: api/Demandas/5
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

        // POST: api/Demandas
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<Demandum>> PostDemandum(Demandum demandum)
        {
          if (_context.Demanda == null)
          {
              return Problem("Entity set 'RailwayContext.Demanda'  is null.");
          }
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

        // DELETE: api/Demandas/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteDemandum(int id)
        {
            if (_context.Demanda == null)
            {
                return NotFound();
            }
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
            return (_context.Demanda?.Any(e => e.CodDemanda == id)).GetValueOrDefault();
        }
    }
}
