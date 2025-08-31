import { Component } from '@angular/core';
import { TaskList } from './components/task-list/task-list';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [TaskList],
  template: `<task-list></task-list>`
})
export class App {}
