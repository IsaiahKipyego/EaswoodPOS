// custom_admin/static/js/main.js

document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('sidebarCollapse').addEventListener('click', function () {
        document.querySelector('.sidebar').classList.toggle('active');
        document.getElementById('content').classList.toggle('active');
    });
});