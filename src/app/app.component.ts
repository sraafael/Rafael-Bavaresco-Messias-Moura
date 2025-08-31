import { Component } from '@angular/core';
import { TaskList } from './components/task-list/task-list'; // caminho ajusta conforme sua pasta

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [TaskList],  // <-- IMPORTANTE!
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})
export class AppComponent {}
