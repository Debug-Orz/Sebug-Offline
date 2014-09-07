function search() {
    var keyword = searchForm.keyword.value;
    if(keyword == "") {
        return;
    } else {
        document.location='/search/' + keyword + '/page/' + '1';
    }
}

function check() {
    if(event.keyCode == 13) {
        search();
    }
}