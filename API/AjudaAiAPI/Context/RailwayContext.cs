﻿using System;
using System.Collections.Generic;
using System.Configuration;
using Microsoft.Data.SqlClient;
using Microsoft.EntityFrameworkCore;

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

    public virtual DbSet<Demandum> Demanda { get; set; }

    public virtual DbSet<Tag> Tags { get; set; }

    public virtual DbSet<Usuario> Usuarios { get; set; }

    public static string StrConexao()
    {
        var builder = WebApplication.CreateBuilder();
        var strCon = 
         builder.Configuration.GetConnectionString("Railway");
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

        modelBuilder.Entity<Tag>(entity =>
        {
            entity.HasKey(e => e.CodTag).HasName("PRIMARY");

            entity.HasIndex(e => e.CodTag, "codTags_UNIQUE").IsUnique();

            entity.Property(e => e.CodTag).HasColumnName("codTag");
            entity.Property(e => e.Nome).HasColumnType("tinytext");
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