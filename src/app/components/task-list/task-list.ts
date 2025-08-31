import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'task-list',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './task-list.html',
  styleUrls: ['./task-list.css']
})
export class TaskList {
  tarefas = [
    { id: 1, descricao: 'Estudar Angular', concluida: false },
    { id: 2, descricao: 'Fazer exercícios', concluida: true }
  ];

  novaTarefa = { descricao: '', concluida: false };
  editandoId: number | null = null;

  adicionarTarefa() {
    if (!this.novaTarefa.descricao.trim()) return;
    this.tarefas.push({
      id: Date.now(),
      descricao: this.novaTarefa.descricao,
      concluida: false
    });
    this.novaTarefa = { descricao: '', concluida: false };
  }

  atualizarStatus(tarefa: any) {
    tarefa.concluida = !tarefa.concluida;
  }

  deletarTarefa(id: number) {
    this.tarefas = this.tarefas.filter(t => t.id !== id);
  }

  editarTarefa(tarefa: any) {
    this.editandoId = tarefa.id;
  }

  salvarEdicao() {
    this.editandoId = null;
  }
}
