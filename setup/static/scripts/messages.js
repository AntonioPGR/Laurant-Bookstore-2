document.getElementById('messages__closeContainer').addEventListener('click', (ev) => {
  ev.preventDefault()

  document.getElementById('messages').style.display = 'none'
})

window.onload = () => {

  console.log('opa')

  setTimeout(() => {
    document.getElementById('messages').style.display = 'none'
  }, 4000)
}