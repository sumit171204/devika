<script>
  import { onMount } from "svelte";
  import { Terminal } from "xterm";
  import "xterm/css/xterm.css";
  import { FitAddon } from "xterm-addon-fit";
  import { agentState } from "$lib/store";

  let terminalElement;
  let terminal;
  let fitAddon;

<<<<<<< HEAD
  onMount(async () => {
    let xterm = await import('xterm');
    let xtermAddonFit = await import('xterm-addon-fit')

    terminal = new xterm.Terminal({
=======
  onMount(() => {
    terminal = new Terminal({
>>>>>>> ce9e082ea6aa57e68ae90e1569a0c096651a4f9d
      disableStdin: true,
      cursorBlink: true,
      convertEol: true,
      rows: 1,
      theme: {
        background: "#d3d3d3",
        foreground: "#000000",
        innerText: "#000000",
        cursor: "#000000",
      },
    });
    fitAddon = new FitAddon();
    terminal.loadAddon(fitAddon);
    terminal.open(terminalElement);
    fitAddon.fit();

    let previousState = {};

    agentState.subscribe((state) => {
      if (state && state.terminal_session) {
        console.log("Terminal state: ", state.terminal_session);

        let command = state.terminal_session.command || 'echo "Waiting..."';
        let output = state.terminal_session.output || "Waiting...";
        let title = state.terminal_session.title || "Terminal";

        // Check if the current state is different from the previous state
        if (
          command !== previousState.command ||
          output !== previousState.output ||
          title !== previousState.title
        ) {
          console.log("Command: ", command);
          addCommandAndOutput(command, output, title);

          // Update the previous state
          previousState = { command, output, title };
        }
      }

      fitAddon.fit();
    });
  });

  function addCommandAndOutput(command, output, title) {
    if (title) {
      document.getElementById("terminal-title").innerText = title;
    }
    terminal.reset();
    terminal.write(`$ ${command}\r\n\r\n${output}\r\n`);
  }
</script>

<div class="flex flex-col border-2 rounded-lg h-1/2">
  <div class="p-2 flex items-center border-b">
    <div class="flex space-x-2 ml-2 mr-4">
      <div class="w-3 h-3 bg-red-500 rounded-full"></div>
      <div class="w-3 h-3 bg-yellow-400 rounded-full"></div>
      <div class="w-3 h-3 bg-green-500 rounded-full"></div>
    </div>
    <span id="terminal-title">Terminal</span>
  </div>
  <div
    id="terminal-content"
    class="h-full w-full rounded-bl-lg "
    bind:this={terminalElement}
  ></div>
</div>

<style>
  #terminal-content :global(.xterm) {
    padding: 10px;
    height: 100%; /* Ensure terminal content height is fixed */
  }

  #terminal-content :global(.xterm-viewport) {
    overflow-y: auto !important;
    height: 100%;
  }

  #terminal-content::-webkit-scrollbar,
  #terminal-content :global(.xterm-viewport)::-webkit-scrollbar {
    width: 4px;
  }

  #terminal-content::-webkit-scrollbar-track,
  #terminal-content :global(.xterm-viewport)::-webkit-scrollbar-track {
    background: #020617;
    border-radius: 10px;
  }

  #terminal-content::-webkit-scrollbar-thumb,
  #terminal-content :global(.xterm-viewport)::-webkit-scrollbar-thumb {
    background: #000000;
    border-radius: 10px;
  }
</style>
