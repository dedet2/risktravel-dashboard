## RiskTravel Dashboard

This repository contains the initial scaffold for the **RiskTravel** admin dashboard. The goal
of this project is to build a robust and scalable web application to manage your
AI governance platform, retreat business, and the suite of automation agents
described in your business plan.

### Features included

* **Next.js 14** with TypeScript for a modern developer experience.
* Basic `index` page and example API route to demonstrate routing.
* Opinionated configuration (`next.config.js` and `tsconfig.json`) following Next.js best practices.

### Getting started

1. Ensure you have Node.js (v18 or later) installed on your machine.
2. Install dependencies:

   ```sh
   cd risktravel-dashboard
   npm install
   ```

3. Start the development server:

   ```sh
   npm run dev
   ```

4. Open your browser and navigate to `http://localhost:3000` to see the home
   page. You should see a simple welcome message indicating that the project
   is set up correctly.

As your project evolves, you’ll replace the placeholder content with pages
showing metrics, forms, tables, and charts powered by your preferred data
sources (Airtable, Postgres, etc.).

### Next steps

* **Set up data sources**: Define schemas for your contacts, leads, and
  revenue streams in a database (Airtable or Postgres). Create API routes to
  fetch and manipulate this data.
* **Design a dashboard UI**: Build reusable components (cards, tables, charts)
  using your preferred UI library (e.g., shadcn/ui). Connect them to your
  data to display real‑time metrics and agent statuses.
* **Integrate automation agents**: Once your API routes are in place, wire up
  your automation scripts (Outreach, Content Repurposer, Booking/CRM, etc.) to
  update your database and trigger notifications.

Feel free to modify the structure and configuration to suit your needs. This
scaffold is intentionally minimal to let you iterate quickly.