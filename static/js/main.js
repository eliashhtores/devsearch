const search_form = document.querySelector('form')
const page_links = document.querySelectorAll('.page-link')

if (search_form) {
    page_links.forEach(page_link => {
        page_link.addEventListener('click', (e) => {
            e.preventDefault()
            const page = page_link.dataset.page
            search_form.innerHTML += `<input type="hidden" name="page" value="${page}">`
            search_form.submit()
        })
    })
}