const tags = document.querySelectorAll('.project-tag')

tags.forEach(tag => {
    tag.addEventListener('click', function (e) {
        e.preventDefault()
        const tag_id = e.target.dataset.tag
        const project_id = e.target.dataset.project

        fetch('/projects/remove-tag/', {
            method: 'DELETE',
            headers: {

            }
        })
    })
})