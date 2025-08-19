import type { NextApiRequest, NextApiResponse } from 'next';

/**
 * Example API route.
 *
 * This demonstrates how to create API endpoints in Next.js. You can delete
 * this file once you build your own endpoints for fetching data from
 * Airtable or orchestrating your automation agents.
 */
export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<{ message: string }>
) {
  res.status(200).json({ message: 'Hello from the RiskTravel API!' });
}