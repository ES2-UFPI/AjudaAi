using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;
using Microsoft.IdentityModel.Protocols;

namespace AjudaAiAPI.Context;

public partial class RailwayContext : DbContext
{
    public RailwayContext()
    {
    }

    public RailwayContext(DbContextOptions<RailwayContext> options)
        : base(options)
    {
    }

    public virtual DbSet<Atreladum> Atrelada { get; set; }

    public virtual DbSet<Comentario> Comentarios { get; set; }

    public virtual DbSet<Demandum> Demanda { get; set; }

    public virtual DbSet<Forum> Forums { get; set; }

    public virtual DbSet<Tag> Tags { get; set; }

    public virtual DbSet<Topico> Topicos { get; set; }

    public virtual DbSet<Usuario> Usuarios { get; set; }

    public static string StrConexao()
    {
        var builder = WebApplication.CreateBuilder();
        var strCon =
         builder.Configuration.GetConnectionString("railwayon");
        return strCon.ToString();
    }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
          => optionsBuilder.UseMySQL(StrConexao());
    

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Atreladum>(entity =>
        {
            entity.HasKey(e => new { e.CodTag, e.CodDemanda }).HasName("PRIMARY");

            entity.HasIndex(e => e.CodDemanda, "codDemanda_UNIQUE").IsUnique();

            entity.HasIndex(e => e.CodTag, "codTag_UNIQUE").IsUnique();

            entity.HasIndex(e => e.CodDemanda, "fk_Atrelada_Demanda1_idx");

            entity.HasIndex(e => e.CodTag, "fk_Atrelada_Tags1_idx");

            entity.Property(e => e.CodTag).HasColumnName("codTag");
            entity.Property(e => e.CodDemanda).HasColumnName("codDemanda");

            entity.HasOne(d => d.CodDemandaNavigation).WithOne(p => p.Atreladum)
                .HasPrincipalKey<Demandum>(p => p.CodDemanda)
                .HasForeignKey<Atreladum>(d => d.CodDemanda)
                .OnDelete(DeleteBehavior.ClientSetNull)
                .HasConstraintName("fk_Atrelada_Demanda1");

            entity.HasOne(d => d.CodTagNavigation).WithOne(p => p.Atreladum)
                .HasForeignKey<Atreladum>(d => d.CodTag)
                .OnDelete(DeleteBehavior.ClientSetNull)
                .HasConstraintName("fk_Atrelada_Tags1");
        });

        modelBuilder.Entity<Comentario>(entity =>
        {
            entity.HasKey(e => new { e.IdComentario, e.CodUsuario, e.IdTopicos }).HasName("PRIMARY");

            entity.ToTable("Comentario");

            entity.HasIndex(e => e.CodUsuario, "fk_Comentario_codUsuario");

            entity.HasIndex(e => e.IdTopicos, "fk_Topicos_idTopicos");

            entity.HasIndex(e => e.IdComentario, "idComentario_UNIQUE").IsUnique();

            entity.Property(e => e.IdComentario).HasColumnName("idComentario");
            entity.Property(e => e.CodUsuario).HasColumnName("codUsuario");
            entity.Property(e => e.IdTopicos).HasColumnName("idTopicos");
            entity.Property(e => e.DataComentario)
                .HasColumnType("date")
                .HasColumnName("data_comentario");
            entity.Property(e => e.Mensagem)
                .HasColumnType("text")
                .HasColumnName("mensagem");

            entity.HasOne(d => d.IdTopicosNavigation).WithMany(p => p.Comentarios)
                .HasPrincipalKey(p => p.IdTopicos)
                .HasForeignKey(d => d.IdTopicos)
                .OnDelete(DeleteBehavior.ClientSetNull)
                .HasConstraintName("fk_Topicos_idTopicos");
        });

        modelBuilder.Entity<Demandum>(entity =>
        {
            entity.HasKey(e => new { e.CodDemanda, e.Solicitante, e.Ajudante }).HasName("PRIMARY");

            entity.HasIndex(e => e.CodDemanda, "codDemanda_UNIQUE").IsUnique();

            entity.HasIndex(e => e.Ajudante, "fk_Demanda_Usuario1_idx");

            entity.HasIndex(e => e.Solicitante, "fk_Demanda_Usuario_idx");

            entity.Property(e => e.CodDemanda).HasColumnName("codDemanda");
            entity.Property(e => e.Descricao).HasColumnType("text");
            entity.Property(e => e.DtAbertura)
                .HasColumnType("date")
                .HasColumnName("dt_Abertura");
            entity.Property(e => e.Grupo)
                .HasMaxLength(1)
                .IsFixedLength();
            entity.Property(e => e.Status).HasMaxLength(20);

            entity.HasOne(d => d.AjudanteNavigation).WithMany(p => p.DemandumAjudanteNavigations)
                .HasForeignKey(d => d.Ajudante)
                .OnDelete(DeleteBehavior.ClientSetNull)
                .HasConstraintName("fk_Demanda_Usuario1");

            entity.HasOne(d => d.SolicitanteNavigation).WithMany(p => p.DemandumSolicitanteNavigations)
                .HasForeignKey(d => d.Solicitante)
                .OnDelete(DeleteBehavior.ClientSetNull)
                .HasConstraintName("fk_Demanda_Usuario");
        });

        modelBuilder.Entity<Forum>(entity =>
        {
            entity.HasKey(e => e.IdForum).HasName("PRIMARY");

            entity.ToTable("Forum");

            entity.HasIndex(e => e.IdForum, "idForum_UNIQUE").IsUnique();

            entity.Property(e => e.IdForum).HasColumnName("idForum");
        });

        modelBuilder.Entity<Tag>(entity =>
        {
            entity.HasKey(e => e.CodTag).HasName("PRIMARY");

            entity.HasIndex(e => e.CodTag, "codTags_UNIQUE").IsUnique();

            entity.Property(e => e.CodTag).HasColumnName("codTag");
            entity.Property(e => e.Nome).HasColumnType("tinytext");
        });

        modelBuilder.Entity<Topico>(entity =>
        {
            entity.HasKey(e => new { e.IdTopicos, e.IdForum, e.CodUsuario }).HasName("PRIMARY");

            entity.HasIndex(e => e.IdForum, "fk_Forum_idForum");

            entity.HasIndex(e => e.CodUsuario, "fk_Topicos_codUsuario");

            entity.HasIndex(e => e.IdTopicos, "idTopicos_UNIQUE").IsUnique();

            entity.Property(e => e.IdTopicos).HasColumnName("idTopicos");
            entity.Property(e => e.IdForum).HasColumnName("idForum");
            entity.Property(e => e.CodUsuario).HasColumnName("codUsuario");
            entity.Property(e => e.DataTopico)
                .HasColumnType("date")
                .HasColumnName("data_topico");
            entity.Property(e => e.Texto).HasColumnType("text");

            entity.HasOne(d => d.CodUsuarioNavigation).WithMany(p => p.Topicos)
                .HasForeignKey(d => d.CodUsuario)
                .OnDelete(DeleteBehavior.ClientSetNull)
                .HasConstraintName("fk_Topicos_codUsuario");

            entity.HasOne(d => d.IdForumNavigation).WithMany(p => p.Topicos)
                .HasForeignKey(d => d.IdForum)
                .OnDelete(DeleteBehavior.ClientSetNull)
                .HasConstraintName("fk_Forum_idForum");
        });

        modelBuilder.Entity<Usuario>(entity =>
        {
            entity.HasKey(e => e.CodUsuario).HasName("PRIMARY");

            entity.ToTable("Usuario");

            entity.HasIndex(e => e.Matricula, "Matricula_UNIQUE").IsUnique();

            entity.HasIndex(e => e.Usuario1, "Usuario_UNIQUE").IsUnique();

            entity.HasIndex(e => e.CodUsuario, "codUsuario_UNIQUE").IsUnique();

            entity.Property(e => e.CodUsuario).HasColumnName("codUsuario");
            entity.Property(e => e.Conhecimento).HasColumnType("text");
            entity.Property(e => e.Curso).HasMaxLength(45);
            entity.Property(e => e.Email).HasMaxLength(100);
            entity.Property(e => e.Nome).HasMaxLength(255);
            entity.Property(e => e.Senha).HasMaxLength(75);
            entity.Property(e => e.Usuario1)
                .HasMaxLength(100)
                .HasColumnName("Usuario");
        });

        OnModelCreatingPartial(modelBuilder);
    }

    partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
}
