function removeUrls() {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    const data = sheet.getDataRange().getValues();
  
    const API_KEY = 'YOUR_API_KEY';
    const siteUrl = 'https://your-website.com';
  
    data.forEach((row, index) => {
      if(index === 0) return;  // Skip header row
      const url = row[0];
  
      const response = UrlFetchApp.fetch(
        `https://www.googleapis.com/webmasters/v3/sites/${encodeURIComponent(siteUrl)}/urlRemovals?key=${API_KEY}`, {
          method: 'post',
          contentType: 'application/json',
          payload: JSON.stringify({
            url: url,
            type: 'URL_REMOVAL'
          }),
          muteHttpExceptions: true
        }
      );
  
      Logger.log(response.getContentText());
    });
  }
  