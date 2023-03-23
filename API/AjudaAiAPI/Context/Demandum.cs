using System;
using System.Collections.Generic;

namespace AjudaAiAPI.Context;

public partial class Demandum
{
    public int CodDemanda { get; set; }

    public string Descricao { get; set; } = null!;

    public string Grupo { get; set; } = null!;

    public DateTime DtAbertura { get; set; }

    public string Status { get; set; } = null!;

    public int Solicitante { get; set; }

    public int Ajudante { get; set; }

    public virtual Usuario AjudanteNavigation { get; set; } = null!;

    public virtual Atreladum? Atreladum { get; set; }

    public virtual Usuario SolicitanteNavigation { get; set; } = null!;
}
