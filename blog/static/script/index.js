var spanContainers = document.querySelectorAll('.title div');
spanContainers.forEach(function (item) {
    var letters = item.children[0].textContent.split('');
    item.innerHTML = "";
    letters.forEach(function (el, index) {
        item.innerHTML += "<span style=\"transition-delay: " + 0.04 * index + "s\">" + el + "</span>";
    });
});
