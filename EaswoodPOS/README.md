
# Eastwood Mobile Phone Accessories

Welcome to the Eastwood Mobile Phone Accessories inventory management system. This project is designed to help manage the inventory, sales, and reporting for a mobile phone accessories store.

  Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

  Overview

Eastwood Mobile Phone Accessories is a Django-based web application that provides a comprehensive solution for managing inventory, sales, and generating reports. It includes functionalities for adding products, managing stock, making sales, and generating sales reports with VAT calculations.

  Features

- Product Management: Add, edit, and delete products.
- Stock Management: Update stock levels for products.
- Sales Management: Record sales transactions and generate receipts.
- Reporting: Generate daily, weekly, monthly, and yearly sales reports.
- VAT Calculation: Automatically calculate VAT for products that include VAT.

  Installation

To get started with the Eastwood Mobile Phone Accessories project, follow these steps:

1. Clone the repository:
   bash
   git clone https://github.com/IsaiahKipyego/eastwoodPOS.git
   cd eastwoodPOS
   

2. Create a virtual environment:
   bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   

3. Install the dependencies:
   bash
   pip install -r requirements.txt
   

4. Apply migrations:
   bash
   python manage.py makemigrations
   python manage.py migrate
   

5. Create a superuser:
   bash
   python manage.py createsuperuser
   

6. Run the development server:
   bash
   python manage.py runserver
   

7. Access the application:
   Open your web browser and go to `http://127.0.0.1:8000`.

  Usage

Adding Products

1. Go to the "Add Product" page.
2. Fill in the product details, including name, description, buying price, selling price, stock, category, VAT inclusion, and POS listing.
3. Click "Save" to add the product.

Generating Sales Reports

1. Go to the "Sales Report" page.
2. Select the desired period (daily, weekly, monthly, yearly, or custom date range).
3. Click "Generate Report" to view the sales report, including total VAT.

  Contributing

We welcome contributions to improve the Eastwood Mobile Phone Accessories project. To contribute:

1. Fork the repository.
2. Create a new branch:
   bash
   git checkout -b feature/your-feature-name
   
3. Make your changes and commit them:
   bash
   git commit -m "Add some feature"
   
4. Push to the branch:
   bash
   git push origin feature/your-feature-name
   
5. Create a pull request.

Please ensure your code follows the project's coding standards and includes appropriate tests.

  License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

  Contact

Creator: Isaiah Kipyego

For any questions or suggestions, please feel free to contact Isaiah Kipyego at kipyegoisaiah@yahoo.com



Happy coding!
