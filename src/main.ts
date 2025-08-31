import { bootstrapApplication } from '@angular/platform-browser';
import { App } from './app/app';
import { importProvidersFrom } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';

bootstrapApplication(App, {
  providers: [importProvidersFrom(BrowserModule, FormsModule)]
})
  .catch(err => console.error(err));
