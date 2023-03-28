using System;
using System.Collections.Generic;

namespace AjudaAiAPI.Context;

public partial class Comentario
{
    public int IdComentario { get; set; }

    public int CodUsuario { get; set; }

    public int IdTopicos { get; set; }

    public DateTime DataComentario { get; set; }

    public string Mensagem { get; set; } = null!;

    public virtual Topico IdTopicosNavigation { get; set; } = null!;
}
