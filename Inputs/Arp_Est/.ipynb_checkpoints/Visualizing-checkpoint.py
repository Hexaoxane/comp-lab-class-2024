{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5f217857-dcd4-4bee-81f1-a8432292ac05",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'pymol'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[2], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mpymol\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m cmd\n\u001b[1;32m      3\u001b[0m \u001b[38;5;66;03m# Load all the PDB structures\u001b[39;00m\n\u001b[1;32m      4\u001b[0m cmd\u001b[38;5;241m.\u001b[39mload(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m/mnt/d/QM_E/week7/Inputs/Arp_Est/test_394f9/test_394f9_unrelaxed_rank_001_alphafold2_ptm_model_4_seed_007.pdb\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmodel_1\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'pymol'"
     ]
    }
   ],
   "source": [
    "from pymol import cmd\n",
    "\n",
    "# Load all the PDB structures\n",
    "cmd.load(\"/mnt/d/QM_E/week7/Inputs/Arp_Est/test_394f9/test_394f9_unrelaxed_rank_001_alphafold2_ptm_model_4_seed_007.pdb\", \"model_1\")\n",
    "cmd.load(\"/mnt/d/QM_E/week7/Inputs/Arp_Est/test_394f9/test_394f9_unrelaxed_rank_002_alphafold2_ptm_model_5_seed_000.pdb\", \"model_2\")\n",
    "cmd.load(\"/mnt/d/QM_E/week7/Inputs/Arp_Est/test_394f9/test_394f9_unrelaxed_rank_003_alphafold2_ptm_model_5_seed_007.pdb\", \"model_3\")\n",
    "cmd.load(\"/mnt/d/QM_E/week7/Inputs/Arp_Est/test_394f9/test_394f9_unrelaxed_rank_004_alphafold2_ptm_model_1_seed_007.pdb\", \"model_4\")\n",
    "cmd.load(\"/mnt/d/QM_E/week7/Inputs/Arp_Est/test_394f9/test_394f9_unrelaxed_rank_005_alphafold2_ptm_model_5_seed_005.pdb\", \"model_5\")\n",
    "\n",
    "# Superimpose the models for visualization\n",
    "cmd.align(\"model_1\", \"model_2\")\n",
    "cmd.align(\"model_1\", \"model_3\")\n",
    "cmd.align(\"model_1\", \"model_4\")\n",
    "cmd.align(\"model_1\", \"model_5\")\n",
    "\n",
    "# Display them as cartoon representation\n",
    "cmd.show(\"cartoon\", \"model_1\")\n",
    "cmd.show(\"cartoon\", \"model_2\")\n",
    "cmd.show(\"cartoon\", \"model_3\")\n",
    "cmd.show(\"cartoon\", \"model_4\")\n",
    "cmd.show(\"cartoon\", \"model_5\")\n",
    "\n",
    "# Color by chain to distinguish each model\n",
    "cmd.color(\"red\", \"model_1\")\n",
    "cmd.color(\"green\", \"model_2\")\n",
    "cmd.color(\"blue\", \"model_3\")\n",
    "cmd.color(\"yellow\", \"model_4\")\n",
    "cmd.color(\"magenta\", \"model_5\")\n",
    "\n",
    "# Set white background\n",
    "cmd.bg_color(\"white\")\n",
    "\n",
    "# Zoom into the structure\n",
    "cmd.zoom()\n",
    "\n",
    "# Save an image\n",
    "cmd.png(\"/mnt/d/QM_E/week7/Images/arp_est_vmd_visualization.png\", dpi=300)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ea741d8d-69ee-45d1-a824-0bac9f749392",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}