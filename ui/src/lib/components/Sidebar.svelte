<<<<<<< HEAD
<div
  class="flex flex-col w-20 h-dvh fixed top-0 left-0 z-10 bg-slate-950 p-4 space-y-4 items-center shadow-2xl shadow-indigo-700"
>
  <div class="p-5 rounded nav-button relative">
    <a href="/">
    <button class="text-gray-400 hover:text-white flex justify-center w-full">
      <i class="fas fa-home fa-lg"></i>
    </button>
  </a>
    <span class="tooltip">Home</span>
  </div>
  <div class="p-5 rounded nav-button relative">
    <a href="/settings">
      <button class="text-gray-400 hover:text-white flex justify-center w-full">
        <i class="fas fa-cog fa-lg"></i>
      </button>
    </a>
    <span class="tooltip">Settings</span> 
  </div>
  <div class="p-5 rounded nav-button relative">
    <button class="text-gray-400 hover:text-white flex justify-center w-full">
      <i class="fas fa-history fa-lg"></i>
    </button>
    <span class="tooltip">Logs</span>
  </div>
=======
<script>
  let navItems = [
    { icon: "fa-home", tooltip: "Home", route: "/" },
    { icon: "fa-cog", tooltip: "Settings", route: "/settings"},
    { icon: "fa-history", tooltip: "Logs", route: "/logs"},
  ];
</script>

<div class="flex flex-col p-4 gap-4 items-center bg-gray-100">
  {#each navItems as item (item.tooltip)}
  <a href = {item.route}>
    <div class="p-4 rounded nav-button relative">
      <button
        class="hover:text-gray-500 flex justify-center w-full hover:transition-colors"
      >
        <i class={`fas ${item.icon} fa-lg`}></i>
      </button>
      <span class="tooltip">{item.tooltip}</span>
    </div>
  </a>
  {/each}
>>>>>>> ce9e082ea6aa57e68ae90e1569a0c096651a4f9d
</div>

<style>
  .tooltip {
    font-size: 12px;
    background-color: black;
    color: white;
    text-align: center;
    border-radius: 100px;
    padding: 5px 10px;
    position: absolute;
    z-index: 1;
    opacity: 0;
    top: 50%;
    left: 90%;
    transform: translateY(-50%);
    transition: opacity 0.3s;
  }

  .nav-button:hover .tooltip {
    visibility: visible;
    opacity: 1;
  }
</style>
