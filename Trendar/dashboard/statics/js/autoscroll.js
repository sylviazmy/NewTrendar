/**
 * Created by I321310 on 1/18/2017.
 */

// store the passage content
var psgContent = [
    "Passage 0 Passage 0 Passage 0 Passage 0",
    "Passage 1 Passage 1 Passage 1 Passage 1",
    "Passage 2 Passage 2 Passage 2 Passage 2",
    "Passage 3 Passage 3 Passage 3 Passage 3",
    "Passage 4 Passage 4 Passage 4 Passage 4",
    "Passage 5 Passage 5 Passage 5 Passage 5",
    "Passage 6 Passage 6 Passage 6 Passage 6",
    "Passage 7 Passage 7 Passage 7 Passage 7",
    "Passage 8 Passage 8 Passage 8 Passage 8",
    "Passage 9 Passage 9 Passage 9 Passage 9"
];

// it will display (maxRowInList - 1) items in the browser
function autoScroll( maxRowInList ) {
    var li = $('#top-hl div ul li');
    var totalHeight =
        parseInt(li.css('margin-top'), 10) +
        parseInt(li.css('margin-bottom'), 10) +
        parseInt(li.css('border-top'), 10) +
        parseInt(li.css('border-bottom'), 10) +
        parseInt(li.css('padding-top'), 10) +
        parseInt(li.css('padding-bottom'), 10) +
        parseInt(li.css('height'), 10);

    var ul = $('#top-hl div ul');
    ul.html('');
    $('#top-hl div').css('height', ((maxRowInList - 1) * totalHeight).toString() + 'px')

    var cells = [];
    psgContent.forEach(function (item) {
        cells.push($('<li>').text(item));
    });

    var cellsInList = [];
    for(var i = 0; i < maxRowInList; i++){
        cellsInList[i] = cells[i];
    }

    cellsInList.forEach(function (item) {
        item.appendTo(ul);
    });

    var appendIndex = maxRowInList;
    function scroll() {
        ul.animate({top:'-' + totalHeight.toString() + 'px'},1000,function () {
            cellsInList.splice(0,1);
            cellsInList.push(cells[appendIndex++]);
            ul.html('');
            ul.css('top','0');
            cellsInList.forEach(function (item) {
                item.appendTo(ul);
            });
            if(appendIndex >= cells.length)
                appendIndex = 0;
            scroll();
        });
    };
    scroll();

    ul.hover(function () {
        ul.stop();
    }, function () {
        scroll();
    });
};

$(document).ready(function () {
        autoScroll(8);
    }
);

