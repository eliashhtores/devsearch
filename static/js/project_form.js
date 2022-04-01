const tags = document.querySelectorAll('.project-tag')

tags.forEach(tag => {
    tag.addEventListener('click', function (e) {
        e.preventDefault()
        const tag_id = e.target.dataset.tag
        const project_id = e.target.dataset.project

        fetch('/api/project/remove-tag/', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(
                { tag_id, project_id }
            )
        })
            .then(response => response.json())
            .then(response => {
                if (response) {
                    e.target.remove()
                }
            })
            .catch(error => console.error(error))
    })
})