document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.book-btn').forEach(btn => {
    btn.onclick = () => handleBooking(btn, 'book');
  });
  document.querySelectorAll('.cancel-btn').forEach(btn => {
    btn.onclick = () => handleBooking(btn, 'cancel');
  });

  async function handleBooking(btn, action) {
    const card = btn.closest('.event-card');
    const eventId = card.dataset.eventId;
    const url = `/${action === 'book' ? 'api/bookings/' : 'api/bookings/'}`
    const method = action === 'book' ? 'POST' : 'DELETE';
    const csrfToken = getCSRFToken();

    try {
      const res = await fetch(action === 'book' ? '/api/bookings/' : `/api/bookings/${eventId}/`, {
        method,
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken,
        },
        body: action === 'book' ? JSON.stringify({ event: eventId }) : null
      });
      if (res.ok) window.location.reload();
      else alert('Action failed');
    } catch (e) { console.error(e); alert('Network error'); }
  }

  function getCSRFToken() {
    return document.cookie.split('; ')
      .find(row => row.startsWith('csrftoken='))
      .split('=')[1];
  }
});
