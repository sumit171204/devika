import {
  agentState,
  internet,
<<<<<<< HEAD
  messages,
  modelList,
  projectList,
=======
  searchEngineList,
>>>>>>> ce9e082ea6aa57e68ae90e1569a0c096651a4f9d
} from "./store";
import { io } from "socket.io-client";

<<<<<<< HEAD
const getApiBaseUrl = () => {
  if (typeof window !== 'undefined') {
    // Client-side code
    const host = window.location.hostname;
    if (host === 'localhost' || host === '127.0.0.1') {
      return 'http://127.0.0.1:1337';
    } else {
      return `http://${host}:1337`;
    }
  } else {
    // Server-side code (Node.js)
    return 'http://127.0.0.1:1337';
  }
};

export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || getApiBaseUrl();

=======
export const API_BASE_URL = "http://127.0.0.1:1337";
export const socket = io(API_BASE_URL);
>>>>>>> ce9e082ea6aa57e68ae90e1569a0c096651a4f9d

export async function fetchInitialData() {
  const response = await fetch(`${API_BASE_URL}/api/data`);
  const data = await response.json();
  projectList.set(data.projects);
  modelList.set(data.models);
  searchEngineList.set(data.search_engines);
  localStorage.setItem("defaultData", JSON.stringify(data));
}

export async function createProject(projectName) {
  await fetch(`${API_BASE_URL}/api/create-project`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ project_name: projectName }),
  });
  projectList.update((projects) => [...projects, projectName]);
}

export async function deleteProject(projectName) {
  await fetch(`${API_BASE_URL}/api/delete-project`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ project_name: projectName }),
  });
}

export async function fetchMessages() {
  const projectName = localStorage.getItem("selectedProject");
  const response = await fetch(`${API_BASE_URL}/api/messages`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ project_name: projectName }),
  });
  const data = await response.json();
  messages.set(data.messages);
}

export async function fetchAgentState() {
  const projectName = localStorage.getItem("selectedProject");
  const response = await fetch(`${API_BASE_URL}/api/get-agent-state`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ project_name: projectName }),
  });
  const data = await response.json();
  agentState.set(data.state);
}

export async function executeAgent(prompt) {
  const projectName = localStorage.getItem("selectedProject");
  const modelId = localStorage.getItem("selectedModel");

  if (!modelId) {
    alert("Please select the LLM model first.");
    return;
  }

  await fetch(`${API_BASE_URL}/api/execute-agent`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      prompt: prompt,
      base_model: modelId,
      project_name: projectName,
    }),
  });

  await fetchMessages();
}

<<<<<<< HEAD
export async function getTokenUsage() {
  const projectName = localStorage.getItem("selectedProject");
  const response = await fetch(`${API_BASE_URL}/api/token-usage?project_name=${projectName}`);
  const data = await response.json();
  return data.token_usage;
}

=======
>>>>>>> ce9e082ea6aa57e68ae90e1569a0c096651a4f9d
export async function getBrowserSnapshot(snapshotPath) {
  const response = await fetch(`${API_BASE_URL}/api/browser-snapshot`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ snapshot_path: snapshotPath }),
  });
  const data = await response.json();
  return data.snapshot;
}

export async function checkInternetStatus() {
  if (navigator.onLine) {
    internet.set(true);
  } else {
    internet.set(false);
  }
}

<<<<<<< HEAD
export async function getSettings() {
  const response = await fetch(`${API_BASE_URL}/api/get-settings`);
=======
export async function fetchSettings() {
  const response = await fetch(`${API_BASE_URL}/api/settings`);
>>>>>>> ce9e082ea6aa57e68ae90e1569a0c096651a4f9d
  const data = await response.json();
  return data.settings;
}

<<<<<<< HEAD
export async function setSettings(newSettings) {
  const response = await fetch(`${API_BASE_URL}/api/set-settings`, {
=======
export async function updateSettings(settings) {
  await fetch(`${API_BASE_URL}/api/settings`, {
>>>>>>> ce9e082ea6aa57e68ae90e1569a0c096651a4f9d
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
<<<<<<< HEAD
    body: JSON.stringify(newSettings),
  });
  const data = await response.json();
  return data;
=======
    body: JSON.stringify(settings),
  });
}

export async function fetchLogs() {
  const response = await fetch(`${API_BASE_URL}/api/logs`);
  const data = await response.json();
  return data.logs;
>>>>>>> ce9e082ea6aa57e68ae90e1569a0c096651a4f9d
}
