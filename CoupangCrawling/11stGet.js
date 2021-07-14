// 비동기 sleep 함수
function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }
  
// 쿠팡 리뷰 데이터 크롤링 함수
async function getReviewsData(numOfReviews) {
    // 리뷰객체들이 저장될 배열
    let reviewList = new Array();

    // 리뷰20개마다 1씩 증가하는 반복문, 리뷰20개를 가져오게 반복하는 반복문
    for (let j =0; j < clickButton; j++) {
        
        for (let i = 0; i < 20; i++){
            try {
              reviews = getReviewsFromHTML();
            } catch (e) {
              console.log(e);
              return reviewList;
            }
        }  
    function clickButton(j) {    
        document
        .querySelector(
          "#review-list-page-area > div > button"
        )
        .click();
    }
}

    
    function createReviewDataObject(reviews, value) {
        let reviewData = Object();
        //작성자 이름
        reviewData.name = getNameFromReview(value);
        // 작성일
        reviewData.date = getDateFromReview(value);
        // 별점
        reviewData.rating = getRatingFromReview(value);
        // 리뷰 내용
        try {
          reviewData.text = getTextFromReview(value);
        } catch (e) {
          console.log(e);
          reviewData.text = "";
        }
    
        return reviewData;
        
        function getTextFromReview(value) {
          return reviews[value].querySelector(
            `#review-list-page-area > ul:nth-child(${j}) > li:nth-child(${i}) > div > div > div.cont_text_wrap.active > p.cont_text`
          ).textContent;
        }
        
        function getRatingFromReview(value) {
          return reviews[value].querySelector(
            `#review-list-page-area > ul:nth-child(${j}) > li:nth-child(${i}) > div > p.grade > span > em`
          ).dataset.rating;
        }
        
        function getDateFromReview(value) {
          return reviews[value].querySelector(
            `#review-list-page-area > ul:nth-child(${j}) > li:nth-child(${i}) > dl > dt`
          ).textContent;
        }
        
        function getNameFromReview(value) {
          return reviews[value].querySelector(
            `#review-list-page-area > ul:nth-child(${j}) > li:nth-child(${i}) > div > p.side > span`
          ).textContent;
        }
    
      }
    
      function getReviewsFromHTML() {
        return document.querySelectorAll(
          `#review-list-page-area > ul:nth-child(${j}) > li:nth-child(${i})`
        );
      }
}



// 리뷰 객체 배열을 json화 한 후 컴퓨터에 저장하는 함수
function getJSONFile(numOfReviews) {
    getReviewsData(numOfReviews).then(function (resolved) {
      let jsonReviews = JSON.stringify(resolved);
      console.log("review_count : " + resolved.length);
      console.save(jsonReviews);
    });
  }

  getJSONFile(3)