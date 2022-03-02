let alertWrappers = document.querySelectorAll('.alert')

alertWrappers.forEach(alertWrapper => {
  alertWrapper.addEventListener('click', () => {
    alertWrapper.style.display = 'none'
  })
})