import { writable } from 'svelte/store';

const getInitialSelectedProject = () => {
  if (typeof window !== 'undefined' && window.localStorage) {
    return localStorage.getItem('selectedProject') || '';
  }
  return '';
};

const getInitialSelectedModel = () => {
  if (typeof window !== 'undefined' && window.localStorage) {
    return localStorage.getItem('selectedModel') || '';
  }
  return '';
};

export const messages = writable([]);

export const selectedProject = writable(getInitialSelectedProject());
export const projectList = writable([]);
<<<<<<< HEAD

export const selectedModel = writable(getInitialSelectedModel());
export const modelList = writable([]);

export const agentState = writable(null);

export const internet = writable(true);

selectedProject.subscribe((value) => {
  if (typeof window !== 'undefined' && window.localStorage) {
    localStorage.setItem('selectedProject', value);
  }
});

selectedModel.subscribe((value) => {
  if (typeof window !== 'undefined' && window.localStorage) {
    localStorage.setItem('selectedModel', value);
  }
});
=======
export const modelList = writable({});
export const searchEngineList = writable([]);
export const agentState = writable(null);
export const internet = writable(true);
export const tokenUsage = writable(0);
>>>>>>> ce9e082ea6aa57e68ae90e1569a0c096651a4f9d
