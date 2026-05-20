// Brewsko Bistro POS - Main JS
function showToast(message, type = 'success') {
  const container = document.getElementById('toastContainer');
  if (!container) return;
  const toast = document.createElement('div');
  toast.className = `toast-message rounded-3xl border px-4 py-3 text-sm shadow-xl shadow-black/20 pointer-events-auto transition-all duration-500 ease-out ${type === 'error' ? 'border-red-500/40 bg-red-500/10 text-red-100' : 'border-brewsko-500/40 bg-brewsko-500/10 text-warmgray-50'}`;
  toast.textContent = message;
  const wrapper = document.createElement('div');
  wrapper.className = 'w-full';
  wrapper.appendChild(toast);
  container.appendChild(wrapper);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(-10px)';
  }, 3000);
  setTimeout(() => wrapper.remove(), 3600);
}

document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.toast-message').forEach(a => {
    setTimeout(() => {
      a.style.opacity = '0';
      a.style.transform = 'translateY(-10px)';
    }, 3000);
  });
});

function filterRows(input, cls) {
  const query = input.value.trim().toLowerCase();
  document.querySelectorAll(`.${cls}`).forEach(row => {
    const text = row.textContent.trim().toLowerCase();
    row.style.display = query && !text.includes(query) ? 'none' : '';
  });
}
