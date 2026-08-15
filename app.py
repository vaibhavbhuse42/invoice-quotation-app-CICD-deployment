from flask import Flask

app = Flask(__name__)


@app.route("/health")
def health():
    return "Application is Healthy!"


@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Invoice & Quotation Management</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, Helvetica, sans-serif;
        }

        body {
            background: #f4f7fb;
            color: #1f2937;
        }

        .navbar {
            background: #1e3a8a;
            color: white;
            padding: 18px 50px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 3px 10px rgba(0,0,0,0.15);
        }

        .navbar h2 {
            font-size: 22px;
        }

        .navbar span {
            font-size: 14px;
            opacity: 0.9;
        }

        .container {
            max-width: 1200px;
            margin: 40px auto;
            padding: 0 20px;
        }

        .welcome {
            background: white;
            padding: 30px;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        }

        .welcome h1 {
            color: #1e3a8a;
            margin-bottom: 10px;
        }

        .welcome p {
            color: #6b7280;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 25px;
            margin-bottom: 30px;
        }

        .card {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
            transition: 0.3s;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.12);
        }

        .icon {
            font-size: 35px;
            margin-bottom: 15px;
        }

        .card h3 {
            margin-bottom: 8px;
            color: #111827;
        }

        .card p {
            color: #6b7280;
            font-size: 14px;
        }

        .actions {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        }

        .actions h2 {
            margin-bottom: 20px;
            color: #1e3a8a;
        }

        .buttons {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }

        button {
            border: none;
            padding: 13px 22px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 15px;
            font-weight: bold;
        }

        .invoice {
            background: #2563eb;
            color: white;
        }

        .quotation {
            background: #16a34a;
            color: white;
        }

        .reports {
            background: #7c3aed;
            color: white;
        }

        button:hover {
            opacity: 0.85;
        }

        footer {
            text-align: center;
            padding: 25px;
            color: #6b7280;
            font-size: 14px;
        }

        @media (max-width: 800px) {
            .cards {
                grid-template-columns: 1fr;
            }

            .navbar {
                padding: 18px 20px;
            }
        }
    </style>
</head>

<body>

    <nav class="navbar">
        <h2>📄 Invoice & Quotation</h2>
        <span>Management System</span>
    </nav>

    <div class="container">

        <div class="welcome">
            <h1>Welcome to Invoice & Quotation Management</h1>
            <p>
                Manage your invoices, quotations and business records
                easily from one place.
            </p>
        </div>

        <div class="cards">

            <div class="card">
                <div class="icon">🧾</div>
                <h3>Invoices</h3>
                <p>Create and manage professional invoices for your customers.</p>
            </div>

            <div class="card">
                <div class="icon">📋</div>
                <h3>Quotations</h3>
                <p>Create quotations and share them with your customers.</p>
            </div>

            <div class="card">
                <div class="icon">📊</div>
                <h3>Reports</h3>
                <p>View and manage your invoice and quotation records.</p>
            </div>

        </div>

        <div class="actions">

            <h2>Quick Actions</h2>

            <div class="buttons">
                <button class="invoice">
                    ➕ Create Invoice
                </button>

                <button class="quotation">
                    ➕ Create Quotation
                </button>

                <button class="reports">
                    📊 View Reports
                </button>
            </div>

        </div>

    </div>

    <footer>
        © 2026 Invoice & Quotation Management App | CI/CD Deployment
    </footer>

</body>
</html>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)