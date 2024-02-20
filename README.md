# Python Flask API for Scraping Amazon and Flipkart

This project is a Python Flask API designed to scrape product information from Amazon and Flipkart websites. It retrieves product details such as title, price, image, and rating from the provided URLs. This API can be integrated into various applications to fetch real-time data from these e-commerce platforms.

## Use API

## Response Format

The API responds with JSON data containing the following fields:

- `title`: The title of the product.
- `currentPrice`: The price of the product(float).
- `img`: The URL of the product image.
- `rating`: The rating of the product(float).
- `company`: The name Of Company.
- `url`:Url Of Product.

Example response:

```json
{
  "title": "Example Product",
  "currentPrice": 19.99,
  "img": "https://example.com/product_image.jpg",
  "rating": 4.5,
  "company": "amazon",
  "url": "https://www.amazon.com/example-product"
}
```

## Clone

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/your_username/your_project.git
   ```

2. Navigate to the project directory:

   ```
   cd your_project
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask API:

   ```
   python app.py
   ```

   ```
   flask --app app run --debug
   ```

2. Once the server is running, you can make HTTP requests to the following endpoints:

   - `/yourHostUrl/?url= copyUrl`

3. Example usage with cURL:

   ```
   curl http://127.0.0.1:5000/?url=https://www.amazon.com/example-product
   ```

## Disclaimer

This project is for educational purposes only. Scraping e-commerce websites may violate their terms of service. Use responsibly and respect the terms and conditions of the websites you scrape.
