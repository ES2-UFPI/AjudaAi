using System;
using System.Collections.Generic;

namespace AjudaAiAPI.Context;

public partial class Usuario
{
    public int CodUsuario { get; set; }

    public int Matricula { get; set; }

    public string Email { get; set; } = null!;

    public string Conhecimento { get; set; } = null!;

    public float? Avaliacao { get; set; }

    public string? Curso { get; set; }

    public string Nome { get; set; } = null!;

    public string Senha { get; set; } = null!;

    public string Usuario1 { get; set; } = null!;

    public float? RankAvaliacao { get; set; }

    public virtual ICollection<Demandum> DemandumAjudanteNavigations { get; } = new List<Demandum>();

    public virtual ICollection<Demandum> DemandumSolicitanteNavigations { get; } = new List<Demandum>();

    public virtual ICollection<Topico> Topicos { get; } = new List<Topico>();
}
