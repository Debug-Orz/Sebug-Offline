function search() {
    var keyword = searchForm.keyword.value;
    if(keyword == "") {
        return;
    } else {
        document.location='/search/' + keyword;
    }
}

function check() {
    if(event.keyCode == 13) {
        alert(1);
        search();
    }
}